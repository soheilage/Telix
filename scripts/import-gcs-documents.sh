#!/usr/bin/env bash
# Imports unstructured documents from Cloud Storage into a Discovery Engine data
# store. Called by Terraform (terraform_data.import_documents); safe to re-run.
#
# Env: PROJECT_ID LOCATION DATA_STORE_ID GCS_URI
set -euo pipefail

: "${PROJECT_ID:?}" "${LOCATION:?}" "${DATA_STORE_ID:?}" "${GCS_URI:?}"

if [[ "${LOCATION}" == "global" ]]; then
  HOST="discoveryengine.googleapis.com"
else
  HOST="${LOCATION}-discoveryengine.googleapis.com"
fi

PARENT="projects/${PROJECT_ID}/locations/${LOCATION}/collections/default_collection/dataStores/${DATA_STORE_ID}/branches/0"
TOKEN=$(gcloud auth application-default print-access-token 2>/dev/null || gcloud auth print-access-token)

echo "Importing ${GCS_URI} into ${PARENT} ..."
RESPONSE=$(curl -sS -X POST \
  -H "Authorization: Bearer ${TOKEN}" \
  -H "Content-Type: application/json" \
  -H "X-Goog-User-Project: ${PROJECT_ID}" \
  "https://${HOST}/v1/${PARENT}/documents:import" \
  -d "{
        \"gcsSource\": { \"inputUris\": [\"${GCS_URI}\"], \"dataSchema\": \"content\" },
        \"reconciliationMode\": \"INCREMENTAL\"
      }")

if grep -q '"error"' <<<"${RESPONSE}"; then
  echo "Import request failed:" >&2
  echo "${RESPONSE}" >&2
  exit 1
fi

OP=$(sed -n 's/.*"name": *"\([^"]*\)".*/\1/p' <<<"${RESPONSE}" | head -1)
echo "Import started: ${OP}"
echo "Indexing typically completes within 5-10 minutes. Check status with:"
echo "  curl -H \"Authorization: Bearer \$(gcloud auth print-access-token)\" https://${HOST}/v1/${OP}"
