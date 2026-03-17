# Dictionary mapping crops to farming tips

FARMING_TIPS = {
    "rice": {
        "irrigation": "Requires constant supply of water. Keep the field flooded in early stages.",
        "soil": "Clayey, loam soil which can hold water is ideal.",
        "climate": "Hot and humid climate with abundant rainfall (150-300 cm) is best."
    },
    "maize": {
        "irrigation": "Needs moderate water. Sensitive to water stagnation.",
        "soil": "Well-drained, fertile loamy soil.",
        "climate": "Requires warm climate for germination and growth."
    },
    "chickpea": {
        "irrigation": "Drought-hardy. Pre-sowing irrigation is important.",
        "soil": "Well-drained, heavy soils. Sensitive to salinity.",
        "climate": "Cool and dry climate."
    },
    "kidneybeans": {
        "irrigation": "Needs consistent moisture but avoid waterlogging.",
        "soil": "Well-drained loamy soil rich in organic matter.",
        "climate": "Cool weather crop, sensitive to extreme heat."
    },
    "pigeonpeas": {
        "irrigation": "Drought-tolerant deep root system. Irrigation during flowering/pod development is helpful.",
        "soil": "Well-drained light to medium soils.",
        "climate": "Warm tropical and subtropical climate."
    },
    "mothbeans": {
        "irrigation": "Highly drought tolerant. Needs very little irrigation.",
        "soil": "Light sandy to loam soils.",
        "climate": "Hot, arid climates are ideal."
    },
    "mungbean": {
        "irrigation": "Sensitive to waterlogging. Needs limited water.",
        "soil": "Well-drained loamy to sandy loam soil.",
        "climate": "Warm season crop, requires dry spell during ripening."
    },
    "blackgram": {
        "irrigation": "Requires moderate moisture. Rainfed mostly.",
        "soil": "Heavy clay to loam soils.",
        "climate": "Warm and humid climate."
    },
    "lentil": {
        "irrigation": "Drought-tolerant but needs moisture during germination.",
        "soil": "Well-drained loamy soils.",
        "climate": "Cool climate."
    },
    "pomegranate": {
        "irrigation": "Regular irrigation during fruiting, can withstand drought.",
        "soil": "Deep loamy and well-drained soils.",
        "climate": "Hot and dry summer, cold winter."
    },
    "banana": {
        "irrigation": "Needs abundant and frequent watering.",
        "soil": "Rich, well-drained soil with plenty of organic matter.",
        "climate": "Warm, humid tropical climate."
    },
    "mango": {
        "irrigation": "Irrigate quickly right after planting. Older trees need less.",
        "soil": "Well-drained lateritic and loamy soils.",
        "climate": "Tropical and subtropical climates."
    },
    "grapes": {
        "irrigation": "Requires carefully managed irrigation, especially during fruit set.",
        "soil": "Well-drained gravelly, sandy loam.",
        "climate": "Warm, dry summers and cool winters."
    },
    "watermelon": {
        "irrigation": "Requires uniform soil moisture. Do not overwater near harvest.",
        "soil": "Well-drained sandy or sandy loam soil.",
        "climate": "Hot and dry climate."
    },
    "muskmelon": {
        "irrigation": "Consistent moisture, but avoid excessive water late in season.",
        "soil": "Sandy loam, rich in organic matter.",
        "climate": "Hot, dry air and plenty of sunshine."
    },
    "apple": {
        "irrigation": "Needs uniform soil moisture, especially in summer.",
        "soil": "Well-drained loamy soil.",
        "climate": "Cool climates with adequate chilling hours."
    },
    "orange": {
        "irrigation": "Needs regular watering but avoid water stagnation.",
        "soil": "Well-drained sandy loam or clay loam.",
        "climate": "Subtropical climate with distinct summer and winter."
    },
    "papaya": {
        "irrigation": "Requires regular moisture but suffers from waterlogging.",
        "soil": "Well-drained sandy loam or loamy soil.",
        "climate": "Tropical crop, requires warmth and humidity."
    },
    "coconut": {
        "irrigation": "Requires abundant water. Needs regular watering in dry months.",
        "soil": "Sandy, loamy, and well-drained soil.",
        "climate": "Warm and humid tropical climate."
    },
    "cotton": {
        "irrigation": "Needs water during flowering and boll formation.",
        "soil": "Deep black or alluvial soils.",
        "climate": "Warm climate with a long frost-free period."
    },
    "jute": {
        "irrigation": "Requires huge amounts of water.",
        "soil": "Alluvial soil is best.",
        "climate": "Hot and very humid climate."
    },
    "coffee": {
        "irrigation": "Requires evenly distributed rainfall; supplementary irrigation if needed.",
        "soil": "Deep, friable, porous soils rich in organic matter.",
        "climate": "Warm and humid climate, shade is preferred."
    }
}

def get_tips(crop_name: str) -> dict:
    """Returns tips for a given crop if available."""
    return FARMING_TIPS.get(crop_name.lower(), {
        "irrigation": "General irrigation needed; maintain moderate moisture.",
        "soil": "Good quality, well-drained soil recommended.",
        "climate": "Adaptable to local conditions, ensure adequate sunlight."
    })
