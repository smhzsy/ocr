def luhn_check(card_number: str) -> bool:
    """
    Validating the Credit Card number with Luhn algorithm.
    :param card_number: The card number to check.
    :return: bool
    """
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False

    digits = [int(digit) for digit in card_number]
    checksum = 0
    even_digit = False

    for digit in reversed(digits):
        if even_digit:
            double_digit = digit * 2
            checksum += double_digit if double_digit < 10 else double_digit - 9
        else:
            checksum += digit
        even_digit = not even_digit

    return checksum % 10 == 0