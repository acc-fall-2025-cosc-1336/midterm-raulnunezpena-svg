def get_mph(kilometers, minutes):
    if kilometers < 0 or minutes <= 0:
        return "Invalid arguments"

    miles = kilometers * 0.621371
    hours = minutes / 60
    mph = miles / hours
    return mph
