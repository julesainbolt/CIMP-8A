
FEET_IN_ONE_METER = 3.2808


def to_meters(feet):
    meters = feet / FEET_IN_ONE_METER
    return meters


def to_feet(meters):
    feet = meters * FEET_IN_ONE_METER
    return feet
