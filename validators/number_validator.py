

def IsValidNumber(number: str) -> bool:
    """
    Checking if the string valid for the regex is really a number.
    :param number: String to check.
    :return: bool
    """
    if not number.isdigit():
        return False
    else:
        return True