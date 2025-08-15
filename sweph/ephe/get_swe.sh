
#!/usr/bin/env bash
set -euo pipefail

EPHE_DIR="sweph/ephe"
mkdir -p "$EPHE_DIR"
cd "$EPHE_DIR"

# Official Swiss Ephemeris FTP mirror (Astrodienst)
BASE_URL="https://www.astro.com/ftp/swisseph/ephe"

echo "Downloading Swiss Ephemeris files to $(pwd) ..."
curl -fL "$BASE_URL/sepl_19.se1" -o "sepl_19.se1"
curl -fL "$BASE_URL/semo_19.se1" -o "semo_19.se1"
curl -fL "$BASE_URL/sepl_20.se1" -o "sepl_20.se1"
curl -fL "$BASE_URL/semo_20.se1" -o "semo_20.se1"

echo "Done. Verify files:"
ls -lh sepl_19.se1 semo_19.se1 sepl_20.se1 semo_20.se1
