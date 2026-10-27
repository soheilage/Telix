#!/usr/bin/env bash
# One-time access preflight for the Gemini Enterprise workshop.
# Verifies that the identity running Terraform has what it needs in the shared
# project the admin created. Fails fast with a readable list of gaps.
#
# Usage: PROJECT_ID=my-project ./scripts/preflight.sh
set -euo pipefail

: "${PROJECT_ID:?Set PROJECT_ID}"

red()   { printf '\033[31m%s\033[0m\n' "$*"; }
green() { printf '\033[32m%s\033[0m\n' "$*"; }
fail=0

echo "== Preflight for project: ${PROJECT_ID}"

# 1. gcloud auth -------------------------------------------------------------
ACCOUNT=$(gcloud auth list --filter=status:ACTIVE --format='value(account)' 2>/dev/null || true)
if [[ -z "${ACCOUNT}" ]]; then
  red "✗ No active gcloud account. Run: gcloud auth login && gcloud auth application-default login"
  exit 1
fi
green "✓ gcloud account: ${ACCOUNT}"

if ! gcloud auth application-default print-access-token >/dev/null 2>&1; then
  red "✗ No Application Default Credentials. Run: gcloud auth application-default login"
  fail=1
fi

# 2. Project visible ------------------------------------------------------------
if ! gcloud projects describe "${PROJECT_ID}" --format='value(projectId)' >/dev/null 2>&1; then
  red "✗ Cannot read project ${PROJECT_ID}. Ask the admin for roles/viewer (at minimum)."
  exit 1
fi
green "✓ Project is visible"

# 3. IAM permissions needed by terraform apply -----------------------------------
# Only project-level permissions can be tested here; bucket-level ones
# (storage.objects.*, storage.buckets.*IamPolicy) are implied by storage.buckets.create
# for the bucket creator in practice.
REQUIRED_PERMS=(
  serviceusage.services.enable
  serviceusage.services.list
  storage.buckets.create
  discoveryengine.dataStores.create
  discoveryengine.engines.create
  discoveryengine.documents.import
  resourcemanager.projects.getIamPolicy
  resourcemanager.projects.setIamPolicy
)
TOKEN=$(gcloud auth application-default print-access-token 2>/dev/null || gcloud auth print-access-token 2>/dev/null)
PERMS_JSON=$(printf '"%s",' "${REQUIRED_PERMS[@]}"); PERMS_JSON="[${PERMS_JSON%,}]"
GRANTED=$(curl -sS -X POST \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  "https://cloudresourcemanager.googleapis.com/v1/projects/${PROJECT_ID}:testIamPermissions" \
  -d "{\"permissions\": ${PERMS_JSON}}" \
  | tr -d ' "\n' | sed -n 's/.*permissions:\[\(.*\)\].*/\1/p' | tr ',' '\n')

missing=()
for p in "${REQUIRED_PERMS[@]}"; do
  grep -qx "${p}" <<<"${GRANTED}" || missing+=("${p}")
done
if ((${#missing[@]})); then
  red "✗ Missing IAM permissions (ask the admin to grant e.g. roles/editor + roles/discoveryengine.admin + roles/resourcemanager.projectIamAdmin):"
  printf '    - %s\n' "${missing[@]}"
  fail=1
else
  green "✓ IAM permissions OK"
fi

# 4. Billing -----------------------------------------------------------------------
if [[ "$(gcloud billing projects describe "${PROJECT_ID}" --format='value(billingEnabled)' 2>/dev/null)" != "True" ]]; then
  red "✗ Billing is not enabled on ${PROJECT_ID} (or you lack billing.resourceAssociations.list)."
  fail=1
else
  green "✓ Billing enabled"
fi

# 5. Gemini Enterprise prerequisites that only an admin can do -----------------------
cat <<EOF

== Manual admin prerequisites (cannot be verified here) — confirm before the workshop:
   • Gemini Enterprise subscription / licenses assigned to participants' Workspace users.
   • Gemini Enterprise > Settings > Identity set to "Google Identity" (Workspace) for this project.
   • Participants' Workspace domain allows Drive & Calendar connectors (Workspace Admin > Apps > Google Cloud).
   • Org policy does not block the Discovery Engine service agent from reading Cloud Storage.
EOF

if ((fail)); then
  red "Preflight FAILED — fix the items above and re-run."
  exit 1
fi
green "Preflight PASSED. You can run: terraform apply -var run_preflight=false  (to skip this check next time)"
