
import json
import random

# Load life path affirmations once
with open("life_path_fomo_map_FULLY_ENHANCED_PARAGRAPHS_LPN_1_to_9.json", "r", encoding="utf-8") as f:
    poetic_affirmation_map = json.load(f)

def get_life_path_affirmation(name, life_path):
    options = poetic_affirmation_map.get(str(life_path), [])
    if not options:
        return f"Dear {name}, your path awaits discovery."
    return random.choice(options).replace("{name}", name)



# Mapping of weak planets to healing fragrances
WEAK_PLANET_FRAGRANCES = {
    "Sun": ["Sandalwood Nirvana", "Sacred Dhupa", "Sage's Blessing"],
    "Moon": ["Vrindavan Pushpa", "Radha Rasa", "Lavender Oil", "Lotus Oil", "Vetiver Oil"],
    "Mars": ["Tapasya Nectar", "Bhakti Kusum", "Tagar Oil"],
    "Mercury": ["Kalpavriksha Moksh"],
    "Jupiter": ["Sage's Blessing", "Sacred Dhupa", "Kamal Sparsh"],
    "Venus": ["Vrindavan Pushpa", "Sandalwood Nirvana", "Kamal Sparsh"],
    "Saturn": ["Myrrh Oil", "Kalpavriksha Moksh", "Bhoomi Aura"],
    "Rahu": ["Patchouli Oil", "Camphor Oil", "Loban Oil"],
    "Ketu": ["Aarti Aroma", "Oud Nirvana", "Tagar Oil"]
}


def get_weak_planet_from_chart(chart, dasha_planets=[]):
    strengths = calculate_planet_strengths(chart, dasha_planets)
    return min(strengths, key=strengths.get)

def get_fragrance_for_weak_planet(planet):
    options = WEAK_PLANET_FRAGRANCES.get(planet, [])
    return random.choice(options) if options else "No weak planet fragrance guidance available at the moment."


import json

# Load soul scent logic from JSON file
with open("soul_scent_logic.json", "r", encoding="utf-8") as f:
    soul_scent_logic = json.load(f)

def get_soul_scent_by_life_path(life_path):
    return soul_scent_logic.get("life_path", {}).get(str(life_path), {})

def get_elemental_profile(element):
    return soul_scent_logic.get("elemental_profile", {}).get(element, {})

def get_planetary_guidance(mahadasha, antardasha):
    key = f"{mahadasha}_{antardasha}"
    return soul_scent_logic.get("planetary_guidance", {}).get(key, {})

from flask import Flask, render_template, request, session


# Mapping Antardasha planets to full Antardasha names
ANTARDASHA_TITLE_MAP = {
    "Sun": "Surya Antardasha",
    "Moon": "Chandra Antardasha",
    "Mars": "Mangal Antardasha",
    "Mercury": "Budha Antardasha",
    "Jupiter": "Guru Antardasha",
    "Venus": "Shukra Antardasha",
    "Saturn": "Shani Antardasha",
    "Rahu": "Rahu Antardasha",
    "Ketu": "Ketu Antardasha"
}

# Mapping planets to their representative weekdays
PLANET_WEEKDAY_MAP = {
    "Sun": "Sunday",
    "Moon": "Monday",
    "Mars": "Tuesday",
    "Mercury": "Wednesday",
    "Jupiter": "Thursday",
    "Venus": "Friday",
    "Saturn": "Saturday",
    "Rahu": "Saturday",
    "Ketu": "Tuesday"
}
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
import datetime
import os
import random


def get_soul_scent(ldn, mahadasha, antardasha):
    # Step 1: Map LDN to ruling planet
    ldn_planet_map = {
        1: "Sun", 2: "Moon", 3: "Jupiter", 4: "Rahu", 5: "Mercury",
        6: "Venus", 7: "Ketu", 8: "Saturn", 9: "Mars"
    }


import json
with open("dasha_guidance_map.json", "r", encoding="utf-8") as f:
    DASHA_GUIDANCE = json.load(f)
import json

# Load dasha sequence and years from external JSON file
with open("dasha_data.json", "r", encoding="utf-8") as f:
    dasha_data = json.load(f)

dasha_sequence = dasha_data["sequence"]
dasha_years = dasha_data["years"]
import swisseph as swe
RAHU_ID = swe.MEAN_NODE  # Rahu (mean node)
KETU_ID = swe.TRUE_NODE  # Ketu (true node)


# Load merged elemental profiles
with open("hybrid_elemental_profiles.json", "r", encoding="utf-8") as f:
    MERGED_ELEMENTAL_PROFILES = json.load(f)

def get_merged_elemental_profile(element):
    return MERGED_ELEMENTAL_PROFILES.get(element, "")

app = Flask(__name__)
app.secret_key = 'your-secret-key'
swe_path = "./ephe"
os.environ["FLATLIB_EPHEMERIS_PATH"] = swe_path
swe.set_ephe_path(swe_path)

# Load dynamic JSONs
with open("planetary_intro_templates.json", "r", encoding="utf-8") as f:
    INTRO_TEMPLATES = json.load(f)

with open("life_path_fomo_map_FULLY_ENHANCED_PARAGRAPHS_LPN_1_to_9.json", "r", encoding="utf-8") as f:
    LIFE_PATH_FOMO_MAP = json.load(f)

def get_strongest_planet(planets):
    return max(planets, key=planets.get)

def get_rashi_lord(rashi):
    rashi_lords = {
        "Aries": "Mars (Mangala)", "Taurus": "Venus (Shukra)", "Gemini": "Mercury (Budha)",
        "Cancer": "Moon (Chandra)", "Leo": "Sun (Surya)", "Virgo": "Mercury (Budha)",
        "Libra": "Venus (Shukra)", "Scorpio": "Mars (Mangala)", "Sagittarius": "Jupiter (Guru)",
        "Capricorn": "Saturn (Shani)", "Aquarius": "Saturn (Shani)", "Pisces": "Jupiter (Guru)"
    }
    return rashi_lords.get(rashi, "Unknown")


def get_current_antardasha(mahadasha_lord, mahadasha_start_jd):
    sequence = ["Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"]
    antardasha_durations = {}
    for lord in sequence:
        proportion = dasha_years[lord] / 120
        antardasha_durations[lord] = proportion * dasha_years[mahadasha_lord] * 365.25

    today_jd = swe.julday(*datetime.datetime.today().timetuple()[:3])
    current_jd = mahadasha_start_jd

    for lord in sequence:
        start = current_jd
        end = start + antardasha_durations[lord]

        if start <= today_jd <= end:
            start_date = swe.revjul(start)
            end_date = swe.revjul(end)
            return (
                lord,
                f"{int(start_date[2])}-{int(start_date[1])}-{int(start_date[0])}",
                f"{int(end_date[2])}-{int(end_date[1])}-{int(end_date[0])}"
            )

        current_jd = end

    return "Unknown", "", ""

    antardashas = []
    current_jd = mahadasha_start_jd
    for lord in sequence:
        start = current_jd
        end = start + antardasha_durations[lord]
        antardashas.append((lord, start, end))
        current_jd = end

    today_jd = swe.julday(*datetime.datetime.today().timetuple()[:3])
    for lord, start, end in antardashas:
        if start <= today_jd <= end:
            start_date = swe.revjul(start)
            end_date = swe.revjul(end)
            return (
                lord,
                f"{int(start_date[2])}-{int(start_date[1])}-{int(start_date[0])}",
                f"{int(end_date[2])}-{int(end_date[1])}-{int(end_date[0])}"
            )

        return "Unknown", "", ""


def get_current_mahadasha(jd, moon_long):
    nakshatra_length = 13.3333
    index = int(moon_long / nakshatra_length)
    lord = dasha_sequence[index % 9]
    position_in_nak = moon_long % nakshatra_length
    percentage = position_in_nak / nakshatra_length
    elapsed = percentage * dasha_years[lord]
    start_jd = jd - (elapsed * 365.25)
    timeline = []
    current_jd = start_jd
    for i in range(100):  # safety loop
        l = dasha_sequence[(index + i) % 9]
        duration = dasha_years[l] * 365.25
        end_jd = current_jd + duration
        timeline.append((l, current_jd, end_jd))
        if swe.julday(*datetime.datetime.today().timetuple()[:3]) < end_jd:
            break
        current_jd = end_jd
    for l, start, end in timeline:
        if start <= swe.julday(*datetime.datetime.today().timetuple()[:3]) <= end:
            start_date = swe.revjul(start)
            end_date = swe.revjul(end)
            return (
                l,
                f"{int(start_date[2])}-{int(start_date[1])}-{int(start_date[0])}",
                f"{int(end_date[2])}-{int(end_date[1])}-{int(end_date[0])}",
                start
            )
    return "Unknown", "", "", jd
def get_vimshottari_dasha(jd, moon_long):
    nakshatra_length = 13.3333
    index = int(moon_long / nakshatra_length)
    lord = dasha_sequence[index % 9]
    position_in_nak = moon_long % nakshatra_length
    percentage = position_in_nak / nakshatra_length
    elapsed = percentage * dasha_years[lord]

    start_jd = jd - (elapsed * 365.25)
    end_jd = start_jd + dasha_years[lord] * 365.25

    start = swe.revjul(start_jd)
    end = swe.revjul(end_jd)
    start_str = f"{int(start[2])}-{int(start[1])}-{int(start[0])}"
    end_str = f"{int(end[2])}-{int(end[1])}-{int(end[0])}"

    return lord, start_str, end_str, start_jd


# === FULL MERGE FROM BEST1.PY ===
def calculate_planet_strengths(chart, dasha_planets=[]):
    from flatlib import const
    planet_const_map = {
        "Sun": const.SUN, "Moon": const.MOON, "Mars": const.MARS,
        "Mercury": const.MERCURY, "Jupiter": const.JUPITER,
        "Venus": const.VENUS, "Saturn": const.SATURN
    }

    exaltation_map = {
        "Sun": "Aries", "Moon": "Taurus", "Mars": "Capricorn",
        "Mercury": "Virgo", "Jupiter": "Cancer", "Venus": "Pisces", "Saturn": "Libra"
    }
    debilitation_map = {
        "Sun": "Libra", "Moon": "Scorpio", "Mars": "Cancer",
        "Mercury": "Pisces", "Jupiter": "Capricorn", "Venus": "Virgo", "Saturn": "Aries"
    }

    strengths = {}
    for planet in planet_const_map:
        obj = chart.get(planet_const_map[planet])
        sign = obj.sign
        strength = 1.0

        if sign == exaltation_map.get(planet):
            strength = 2.7
        elif sign == debilitation_map.get(planet):
            strength = 0.6
        elif sign == obj.sign:
            strength = 2.2

        if planet in dasha_planets:
            strength += 0.3

        strengths[planet] = round(min(3.0, strength), 2)
    return strengths



def calculate_dominant_element(chart, rahu_sign=None, ketu_sign=None):
    from collections import Counter
    from flatlib import const

    sign_element_map = {
        "Aries": "Fire", "Leo": "Fire", "Sagittarius": "Fire",
        "Taurus": "Earth", "Virgo": "Earth", "Capricorn": "Earth",
        "Gemini": "Air", "Libra": "Air", "Aquarius": "Air",
        "Cancer": "Water", "Scorpio": "Water", "Pisces": "Water"
    }

    element_counter = Counter()

    # Weighted importance
    ascendant = chart.get(const.ASC).sign
    moon = chart.get(const.MOON).sign
    sun = chart.get(const.SUN).sign

    element_counter[sign_element_map[ascendant]] += 2
    element_counter[sign_element_map[moon]] += 2
    element_counter[sign_element_map[sun]] += 1.5

    for planet_key in [const.MERCURY, const.VENUS, const.MARS, const.JUPITER, const.SATURN]:
        sign = chart.get(planet_key).sign
        element_counter[sign_element_map[sign]] += 1

    dominant = element_counter.most_common(1)[0][0]

    element_advice = {
        "Fire": "Practice cooling breathwork and grounding rituals to temper excess drive.",
        "Water": "Balance your empathy with structured expression — journaling, creative flow.",
        "Earth": "Invite flexibility into your day — change is also growth.",
        "Air": "Ground yourself with nature walks and mindful breathing.",
        "Ether": "Anchor your spiritual energy with body-based routines and simplicity."
    }

    if rahu_sign: element_counter[sign_element_map[rahu_sign]] += 1
    if ketu_sign: element_counter[sign_element_map[ketu_sign]] += 1
    return dominant, element_advice.get(dominant, "")

def get_balanced_guidance(birth, current):
    if birth == current:
        return "Your elemental energy is balanced, but may become stagnant. Introduce complementary energy."
    else:
        return f"Born with {birth} strength, you are currently experiencing {current} influence. Rebalance through mindful rituals."




from flask import Flask, render_template, request, session
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
import datetime
import os
import random
import json


def add_elemental_blessing(result):
    import json
    element = result.get("current_element", "Air")
    with open("elemental_display_fragrance_map.json", "r", encoding="utf-8") as f:
        fragrance_map = json.load(f)
    result["element_balance_advice"] = {
        "Fire": "Practice cooling breathwork and grounding rituals to temper excess drive.",
        "Water": "Balance your empathy with structured expression — journaling, creative flow.",
        "Earth": "Invite flexibility into your day — change is also growth.",
        "Air": "Ground yourself with nature walks and mindful breathing.",
        "Ether": "Anchor your spiritual energy with body-based routines and simplicity."
    }.get(element, "")
    result["fragrance_inspired_name"] = fragrance_map.get(element, {}).get("name", "")
    result["fragrance_poetic_description"] = fragrance_map.get(element, {}).get("poetic", "")
    balance_advice = {
        "Fire": "Practice cooling breathwork and grounding rituals to temper excess drive.",
        "Water": "Balance your empathy with structured expression — journaling, creative flow.",
        "Earth": "Invite flexibility into your day — change is also growth.",
        "Air": "Ground yourself with nature walks and mindful breathing.",
        "Ether": "Anchor your spiritual energy with body-based routines and simplicity."
    }

    fragrances = {
        "Fire": ("Agnideva", "Ignite your soul with Agnideva — a fragrance of purpose, passion, and sacred transformation."),
        "Water": ("Jalasākti", "Let Jalasākti ripple through your being — nurturing calm, empathy, and emotional strength."),
        "Earth": ("Prithvismaran", "Ground your energy with Prithvismaran — the scent of stability, resilience, and inner rootedness."),
        "Air": ("Vāyutattva", "Breathe in the lightness of Vāyutattva — the scent of clarity, flow, and freedom under Ayoura Sky."),
        "Ether": ("Ākāsha Jyoti", "Awaken your spirit with Ākāsha Jyoti — an ethereal blend of space, silence, and divine connection.")
    }

    result["element_balance_advice"] = {
    "Fire": "Practice cooling breathwork and grounding rituals to temper excess drive.",
    "Water": "Balance your empathy with structured expression — journaling, creative flow.",
    "Earth": "Invite flexibility into your day — change is also growth.",
    "Air": "Ground yourself with nature walks and mindful breathing.",
    "Ether": "Anchor your spiritual energy with body-based routines and simplicity."
}.get(result.get("current_element", "Air"), "")

    


    fragrances = {
        "Fire": ("Agnideva", "Ignite your soul with Agnideva — a fragrance of purpose, passion, and sacred transformation."),
        "Water": ("Jalasākti", "Let Jalasākti ripple through your being — nurturing calm, empathy, and emotional strength."),
        "Earth": ("Prithvismaran", "Ground your energy with Prithvismaran — the scent of stability, resilience, and inner rootedness."),
        "Air": ("Vāyutattva", "Breathe in the lightness of Vāyutattva — the scent of clarity, flow, and freedom under Ayoura Sky."),
        "Ether": ("Ākāsha Jyoti", "Awaken your spirit with Ākāsha Jyoti — an ethereal blend of space, silence, and divine connection.")
    }

    result["element_balance_advice"] = balance_advice.get(element, "")
    fragrance = fragrances.get(element, ("", ""))
    result["fragrance_inspired_name"] = fragrance[0]
    result["fragrance_poetic_description"] = fragrance[1]



# Load merged elemental profiles
with open("hybrid_elemental_profiles.json", "r", encoding="utf-8") as f:
    HYBRID_ELEMENTAL_PROFILES = json.load(f)

def get_hybrid_elemental_profile(element):
    return HYBRID_ELEMENTAL_PROFILES.get(element, {"intro": "", "insights": []})

app = Flask(__name__)
app.secret_key = 'your-secret-key'
swe_path = "./ephe"
os.environ["FLATLIB_EPHEMERIS_PATH"] = swe_path

# Load dynamic JSONs
with open("planetary_intro_templates.json", "r", encoding="utf-8") as f:
    INTRO_TEMPLATES = json.load(f)

with open("life_path_fomo_map_FULLY_ENHANCED_PARAGRAPHS_LPN_1_to_9.json", "r", encoding="utf-8") as f:
    LIFE_PATH_FOMO_MAP = json.load(f)

def get_strongest_planet(planets):
    return max(planets, key=planets.get)

def get_rashi_lord(rashi):
    rashi_lords = {
        "Aries": "Mars (Mangala)", "Taurus": "Venus (Shukra)", "Gemini": "Mercury (Budha)",
        "Cancer": "Moon (Chandra)", "Leo": "Sun (Surya)", "Virgo": "Mercury (Budha)",
"Libra": "Venus (Shukra)", "Scorpio": "Mars (Mangala)", "Sagittarius": "Jupiter (Guru)",
        "Capricorn": "Saturn (Shani)", "Aquarius": "Saturn (Shani)", "Pisces": "Jupiter (Guru)"
    }
    return rashi_lords.get(rashi, "Unknown")



def generate_intro(result, strongest_planet=None):
    import random
    import json

    # Load theme mapping
    with open("life_path_theme_map.json", "r", encoding="utf-8") as tf:
        life_path_to_theme = json.load(tf)

    with open("poetic_theme_openers.json", "r", encoding="utf-8") as pf:
        theme_openers = json.load(pf)

    # Determine life path number and theme
    life_path = str(result.get("life_path", "9"))
    theme = life_path_to_theme.get(life_path, "Spiritual")
    openers = theme_openers.get(theme, theme_openers["Spiritual"])
    opener = random.choice(openers).format(place=result["place"], name=result["name"])

    # Compose poetic intro
    return (
        f"{opener}, your divine, karmic journey began on {result['dob']} at {result['tob']} — "
        f"a radiant soul born under the sacred alignment of {result['ascendant']}, guided by the Moon’s nurturing presence in {result['moon_sign']}, "
        f"and illuminated by the Sun’s grace in {result['sun_sign']}. This cosmic configuration reflects your emotional wisdom, karmic clarity, and graceful purpose — "
        f"a soul destined to uplift, heal, and serve with intellect, compassion, and devotion."



    )
def get_rahu_ketu_signs(jd, lat, lon):
    rahu_pos = swe.calc_ut(jd, RAHU_ID)[0][0]
    ketu_pos = (rahu_pos + 180.0) % 360.0

    signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    rahu_sign = signs[int(rahu_pos // 30)]
    ketu_sign = signs[int(ketu_pos // 30)]

    return rahu_sign, ketu_sign


# Load birth and imbalance element paragraphs
with open("birth_element_paragraphs.json", "r", encoding="utf-8") as f:
    birth_element_map = json.load(f)
with open("elemental_paragraphs.json", "r", encoding="utf-8") as f:
    imbalance_map = json.load(f)
with open("elemental_transition_templates.json", "r", encoding="utf-8") as f:
    transition_templates = json.load(f)

def build_elemental_intro(birth_element, current_element, ascendant, moon_sign):
    birth_para = birth_element_map[birth_element].format(
        ascendant=ascendant,
        moon_sign=moon_sign
    )

    if birth_element == current_element:
        transition_line = random.choice(transition_templates["balanced_transitions"]).format(
            birth_element=birth_element
        )
    else:
        transition_line = random.choice(transition_templates["imbalanced_transitions"]).format(
            birth_element=birth_element,
            current_element=current_element
        )

    # ✅ Add dynamic fragrance name using current_element
    with open("elemental_display_fragrance_map.json", "r", encoding="utf-8") as f:
        fragrance_map = json.load(f)
    fragrance_name = fragrance_map.get(current_element, {}).get("name", "a sacred fragrance")

    imbalance_para = imbalance_map[current_element].format(
        ascendant=ascendant,
        moon_sign=moon_sign,
        fragrance=fragrance_name
    )

    return f"<b>🔥 Dominant Personality Element:</b> {birth_para}<br><br>{transition_line}<br><br>{imbalance_para}"


@app.route("/", methods=["GET", "POST"        ])
def index():
    if request.method == "POST":
        latitude = request.form.get("latitude", "").strip()
        longitude = request.form.get("longitude", "").strip()
        if not latitude or not longitude:
            return render_template("blessings.html", result={"error": "Location not found. Please select your city and state from suggestions."},
        antardasha_title=ANTARDASHA_TITLE_MAP.get(result['antardasha'], result['antardasha']),
        antardasha_weekday=PLANET_WEEKDAY_MAP.get(result['antardasha'], 'Unknown'))
        try:
            lat = float(latitude)
            lon = float(longitude)
        except ValueError:
            return render_template("blessings.html", result={"error": "Invalid location format. Please re-select the suggested location."})
        name = request.form["name"]
        gender = request.form["gender"]
        dob = request.form["dob"]
        tob = request.form["tob"]
        place = request.form.get("pob", "")



        chart_time = Datetime(dob.replace("-", "/"), tob, "+05:30")
        pos = GeoPos(lat, lon)
        chart = Chart(chart_time, pos)
    
        jd = swe.julday(int(dob.split("-")[0]), int(dob.split("-")[1]), int(dob.split("-")[2]))
        rahu_sign, ketu_sign = get_rahu_ketu_signs(jd, lat, lon)
    
        # Strong element (from birth chart)
        birth_element, _ = calculate_dominant_element(chart, rahu_sign, ketu_sign)
    
        # Weak element (from current time)
        now = datetime.datetime.now()
        now_dt = Datetime(now.strftime("%Y/%m/%d"), now.strftime("%H:%M"), "+05:30")
        now_chart = Chart(now_dt, pos)
        current_element, _ = calculate_dominant_element(now_chart, rahu_sign, ketu_sign)
    
        # Interpretation
        derived_element = get_balanced_guidance(birth_element, current_element)
    
        asc = chart.get(const.ASC)
        moon = chart.get(const.MOON)
        sun = chart.get(const.SUN)
    
        moon_deg = moon.lon
        nakshatras = [
        ("Ashwini", 0.0, 13.3333), ("Bharani", 13.3333, 26.6666), ("Krittika", 26.6666, 40.0),
        ("Rohini", 40.0, 53.3333), ("Mrigashira", 53.3333, 66.6666), ("Ardra", 66.6666, 80.0),
        ("Punarvasu", 80.0, 93.3333), ("Pushya", 93.3333, 106.6666), ("Ashlesha", 106.6666, 120.0),
        ("Magha", 120.0, 133.3333), ("Purva Phalguni", 133.3333, 146.6666), ("Uttara Phalguni", 146.6666, 160.0),
        ("Hasta", 160.0, 173.3333), ("Chitra", 173.3333, 186.6666), ("Swati", 186.6666, 200.0),
        ("Vishakha", 200.0, 213.3333), ("Anuradha", 213.3333, 226.6666), ("Jyeshtha", 226.6666, 240.0),
        ("Mula", 240.0, 253.3333), ("Purva Ashadha", 253.3333, 266.6666), ("Uttara Ashadha", 266.6666, 280.0),
        ("Shravana", 280.0, 293.3333), ("Dhanishta", 293.3333, 306.6666), ("Shatabhisha", 306.6666, 320.0),
        ("Purva Bhadrapada", 320.0, 333.3333), ("Uttara Bhadrapada", 333.3333, 346.6666), ("Revati", 346.6666, 360.0)
    ]
        nakshatra = next((n for n, start, end in nakshatras if start <= moon_deg < end), "Unknown")
    
        digits = [int(d) for d in dob.replace("-", "")]
        while len(digits) > 1:
            digits = [int(d) for d in str(sum(digits))]
        life_path = digits[0]
    
        # Calculate Soul Scent
        ldn = life_path
        mahadasha_lord, mahadasha_start_str, mahadasha_end_str, mahadasha_start_jd = get_current_mahadasha(jd, moon.lon)
        antardasha_lord, antardasha_start_str, antardasha_end_str = get_current_antardasha(mahadasha_lord, mahadasha_start_jd)
        soul_scent = get_soul_scent(ldn, mahadasha_lord, antardasha_lord)
        fomo_list = LIFE_PATH_FOMO_MAP.get(str(life_path), [        ])
        life_path_fomo = random.choice(fomo_list).format(name=name) if fomo_list else ""
    
        
        dasha_planets = ["Venus", "Mercury"]
        planet_scores = calculate_planet_strengths(chart, dasha_planets)
        strongest_planet = get_strongest_planet(planet_scores)
    
        planet_to_element = {
            "Sun": "Fire", "Mars": "Fire", "Moon": "Water",
            "Venus": "Water", "Mercury": "Air", "Saturn": "Earth", "Jupiter": "Ether"
        }
        element = birth_element  # This aligns all fragrance and advice logic with the *current energetic state*
    
        base_score = (planet_scores[strongest_planet] / 3.0) * 100
        alignment_score = min(100, max(60, int(base_score + random.randint(-5, 5))))
    
    
        today = datetime.datetime.now()
        mahadasha_start = today - datetime.timedelta(days=365 * 3)
        mahadasha_end = today + datetime.timedelta(days=365 * 4)
        antardasha_start = today - datetime.timedelta(days=180)
        antardasha_end = today + datetime.timedelta(days=365)
    
        rashi_lord = get_rashi_lord(moon.sign)
    
        # Remedies based on Dasha planets
        remedies = [
            {"planet": "Mercury", "effect": "Overthinking, scattered energy", "fragrance": "Shanti Chaitanya"},
            {"planet": "Venus", "effect": "Creative block, emotional dullness", "fragrance": "Radha Rasa"}
        ]
    
    
        result = {
            "name": name, "gender": gender, "dob": dob, "tob": tob, "place": place,
            "latitude": lat, "longitude": lon, "ascendant": asc.sign,

        # Set Offering To based on Ascendant Lord and deity
        
 "moon_sign": moon.sign,
            "sun_sign": sun.sign, "nakshatra": nakshatra, "life_path": life_path,
            "life_path_fomo": life_path_fomo,
            "element": element, "rashi_lord": rashi_lord,
            "mahadasha": mahadasha_lord,
            "mahadasha_start": mahadasha_start_str,
            "antardasha_start": antardasha_start_str,
            "mahadasha_end": mahadasha_end_str,
            "antardasha": antardasha_lord,
            "antardasha_end": antardasha_end_str,
            "remedies": remedies,
            "fragrance_name": "Vrindavan Pushpa", "offering_to": "ShivShakti",
            "duration": "Daily through Mercury Antardasha (until 2026)",
            "ritual": "Apply fragrance to wrists and heart center. Sit in quiet reflection. Offer it near Shivling.",
            "alignment_score": alignment_score,
            "birth_element": birth_element,
        "current_element": current_element,
    "derived_element": derived_element,
    "intro_paragraph": generate_intro({
    "name": name,
    "place": place,
    "dob": dob,
    "tob": tob,  # ✅ This was missing!
    "ascendant": asc.sign,

        # Set Offering To based on Ascendant Lord and deity
        

    "moon_sign": moon.sign,
    "sun_sign": sun.sign,
    "birth_element": birth_element,
    "current_element": current_element,
    "derived_element": derived_element
    }, strongest_planet)
    }
    
        result["merged_elemental_html"] = get_merged_elemental_profile(element)
    
    # 🧠 DEBUG: Pause before weak planet fragrance


        hybrid_profile = get_hybrid_elemental_profile(element)
        result["elemental_intro"] = build_elemental_intro(birth_element, current_element, asc.sign, moon.sign)
        result["elemental_insights"] = hybrid_profile.get("insights", [])
        if result["elemental_insights"]:
            result["random_elemental_insight"] = random.choice(result["elemental_insights"])
        else:
            result["random_elemental_insight"] = None
    
        add_elemental_blessing(result)
        key = f"{mahadasha_lord}_{antardasha_lord}".title()
        result["dasha_guidance"] = DASHA_GUIDANCE.get(key, "Guidance not available.")
        result['weak_planet'] = get_weak_planet_from_chart(chart, dasha_planets)
        result['weak_fragrance'] = get_fragrance_for_weak_planet(result['weak_planet'])
        result["score"] = result["alignment_score"]
        
    


        
        antardasha_deity_map = {
            "Sun": "Surya (Sun) – Lord Surya / Rama",
            "Moon": "Chandra (Moon) – Goddess Parvati / Gauri",
            "Mars": "Mangala (Mars) – Lord Subramanya / Hanuman",
            "Mercury": "Budha (Mercury) – Lord Vishnu / Narayana",
            "Jupiter": "Guru (Jupiter) – Lord Brihaspati / Dakshinamurthy",
            "Venus": "Shukra (Venus) – Goddess Lakshmi / Lord Krishna",
            "Saturn": "Shani (Saturn) – Lord Shani / Kala Bhairava",
            "Rahu": "Rahu – Goddess Durga / Bhairavi",
            "Ketu": "Ketu – Lord Ganesha / Matsya"
        }
        result["offering_to"] = antardasha_deity_map.get(result["antardasha"], "Lord Shiva – Devon ke Dev")

        session['blessing_result'] = json.dumps(result)

        # 🌸 Add Mahadasha & Antardasha fragrance lookups
        maha_frag = get_fragrance_for_weak_planet(result['mahadasha'])
        if '(' in maha_frag:
            maha_frag = maha_frag.split('(')[1].rstrip(')')
        anta_frag = get_fragrance_for_weak_planet(result['antardasha'])
        if '(' in anta_frag:
            anta_frag = anta_frag.split('(')[1].rstrip(')')

        # ✅ Final return with all values passed
        return render_template("blessings_result_final.html", result=result, maha_frag=maha_frag, anta_frag=anta_frag)

    
    return render_template("blessings.html")

if __name__ == "__main__":
    app.run(debug=False)


def get_fragrance_for_weak_planet(weak_planet, json_path="weak_planet_fragrance.json"):
    import random
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            mapping = json.load(f)

        fragrances = mapping.get(weak_planet, [])
        if not fragrances:
            return "No fragrance found for this planet."
        return random.choice(fragrances)

    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/test-weak-fragrance")
def test_weak_fragrance():
    weak_planet = request.args.get("planet", "Saturn")
    fragrance = get_fragrance_for_weak_planet(weak_planet)
    return f"<h2>Healing Fragrance for {weak_planet}:<br><br>{fragrance}</h2>"
        
