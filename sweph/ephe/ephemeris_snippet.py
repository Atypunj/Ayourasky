
# ephemeris_snippet.py
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
