
Swiss Ephemeris Setup (Ayoura Sky)
==================================

This package contains scripts and code snippets to download and install the minimal Swiss Ephemeris data files
needed for charts around 1900–2099, and to configure your Flask app to use them.

Files you will download (not included here):
  - sepl_19.se1   (Planets 1900–1999)
  - semo_19.se1   (Moon 1900–1999)
  - sepl_20.se1   (Planets 2000–2099)
  - semo_20.se1   (Moon 2000–2099)

Where to place them:
  sweph/ephe/

How to fetch automatically (Linux / macOS):
  1) Make script executable:
     chmod +x get_swe.sh
  2) Run it from this folder:
     ./get_swe.sh

How to fetch automatically (Windows PowerShell):
  1) Right-click 'get_swe.ps1' > Run with PowerShell (or run: powershell -ExecutionPolicy Bypass -File .\get_swe.ps1)

After files are present, add this snippet near the top of your app.py (before any Chart calls):

    import os
    from flatlib import ephem
    try:
        import swisseph as swe
        EPHE_PATH = os.path.join(os.path.dirname(__file__), "sweph", "ephe")
        if os.path.isdir(EPHE_PATH):
            swe.set_ephe_path(EPHE_PATH)
            ephem.setEphem(ephem.SWISSEPH)
        else:
            ephem.setEphem(ephem.MOSHIER)
    except Exception:
        ephem.setEphem(ephem.MOSHIER)

If you cannot or do not wish to download the files, delete Swiss setup lines and keep:
    from flatlib import ephem
    ephem.setEphem(ephem.MOSHIER)

Notes:
- Data files are hosted by the official Swiss Ephemeris project (Astrodienst).
- If the specific URLs change, browse: https://www.astro.com/ftp/swisseph/ephe/
