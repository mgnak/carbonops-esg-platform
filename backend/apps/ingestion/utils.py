UNIT_CONVERSION = {
    "L": 1,
    "GAL": 3.785,
    "KWH": 3.6,
}


EMISSION_FACTORS = {
    "diesel": 2.68,
    "electricity": 0.82,
    "flight": 0.15,
}


def normalize_value(value, unit):

    factor = UNIT_CONVERSION.get(
        unit.upper(),
        1
    )

    return value * factor


def calculate_co2e(activity_type, normalized_value):

    factor = EMISSION_FACTORS.get(
        activity_type.lower(),
        1
    )

    return normalized_value * factor