import datetime

def get_current_datetime():
    """Returns the current date and time as a string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_float(value_if_allowed):
    """ Validate that the input is a float number """
    if value_if_allowed in ["", "-", ".", "-."]:
        return True
    try:
        float(value_if_allowed)
        return True
    except ValueError:
        return False
