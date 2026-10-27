#!/usr/bin/env bash
# Prints a one-click Google Calendar "template" link that pre-fills the event
# participants create in Task 1. No API access needed — it is just a URL.
#
# Usage: ./scripts/calendar-link.sh            # start = next full hour + 2h (UTC), 30 min long
#        ./scripts/calendar-link.sh 20261105T100000Z 20261105T103000Z
set -euo pipefail

TITLE="Cymbal Foods - Marketing Strategy Meeting"
DETAILS="Review Q1 2026 marketing campaign performance (SPRING25, EMAIL0325, GOOGLEADS01) and agree on next quarter's plan. Prep: latest marketing data and customer feedback."

if [[ $# -eq 2 ]]; then
  START=$1; END=$2
else
  # Next full hour + 2h, in UTC, so it is at least one hour in the future.
  START=$(date -u -d "$(date -u +%Y-%m-%dT%H:00:00) + 2 hour" +%Y%m%dT%H%M%SZ)
  END=$(date -u -d "$(date -u +%Y-%m-%dT%H:00:00) + 2 hour 30 minutes" +%Y%m%dT%H%M%SZ)
fi

urlencode() { python3 -c 'import sys, urllib.parse; print(urllib.parse.quote(sys.argv[1]))' "$1"; }

echo "https://calendar.google.com/calendar/render?action=TEMPLATE&text=$(urlencode "${TITLE}")&details=$(urlencode "${DETAILS}")&dates=${START}/${END}"
