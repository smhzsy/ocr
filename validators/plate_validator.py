def IsValidPlate(plate: str):
    city = int(plate[:2])
    if city > 82:
        return False
    return True
