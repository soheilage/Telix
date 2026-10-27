#!/usr/bin/env bash
# Fills the <PLACEHOLDER> tokens in docs/ from `terraform output` plus the two
# values Terraform cannot know (the web-app URL and the calendar link).
#
# Usage (from repo root, after `terraform apply`):
#   ./scripts/fill-placeholders.sh "<GEMINI_ENTERPRISE_APP_URL>" ["<CALENDAR_TEMPLATE_LINK>"]
#
# The web-app URL is copied from the app's console Overview page
# ("Your Gemini Enterprise webapp is ready"). If the calendar link is omitted,
# scripts/calendar-link.sh is run to generate one.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
APP_URL="${1:?Usage: $0 <GEMINI_ENTERPRISE_APP_URL> [<CALENDAR_TEMPLATE_LINK>]}"
CAL_URL="${2:-$("${ROOT}/scripts/calendar-link.sh")}"

tf() { terraform -chdir="${ROOT}/terraform" output -raw "$1"; }

PROJECT_ID=$(tf project_id)
LOCATION=$(tf location)
BUCKET=$(tf bucket_name)
BUCKET_URL=$(tf bucket_console_url)
APP_CONSOLE_URL=$(tf app_console_url)
DS_URL=$(tf data_stores_console_url)

for f in "${ROOT}"/docs/*.md; do
  sed -i \
    -e "s|<PROJECT_ID>|${PROJECT_ID}|g" \
    -e "s|<LOCATION>|${LOCATION}|g" \
    -e "s|<BUCKET_NAME>|${BUCKET}|g" \
    -e "s|<BUCKET_CONSOLE_URL>|${BUCKET_URL}|g" \
    -e "s|<APP_CONSOLE_URL>|${APP_CONSOLE_URL}|g" \
    -e "s|<DATA_STORES_CONSOLE_URL>|${DS_URL}|g" \
    -e "s|<GEMINI_ENTERPRISE_APP_URL>|${APP_URL}|g" \
    -e "s|<CALENDAR_TEMPLATE_LINK>|${CAL_URL}|g" \
    "$f"
done

left=$(grep -ho '<[A-Z_]*>' "${ROOT}"/docs/*.md | sort -u || true)
if [[ -n "${left}" ]]; then
  echo "Warning: unresolved placeholders remain:"; echo "${left}"
else
  echo "All placeholders filled in docs/."
fi
