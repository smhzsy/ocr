def IsValidPlate(plate: str) -> bool:
    """
    Check if the plate number is valid.
    :param plate: Plate number to check.
    :return:
    """
    city = int(plate[:2])
    if city > 82:
        return False
    return True
