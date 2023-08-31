
dont_accept_values = (
    '11111111110',
    '22222222220',
    '33333333330',
    '44444444440',
    '55555555550',
    '66666666660',
    '77777777770',
    '88888888880',
    '99999999990'
)


def IsValidID(tckn: str) -> bool:
    """
    Checking if the ID number is valid.
    :param tckn: ID to check.
    :return: bool
    """
    if tckn in dont_accept_values:
        return False
    if len(tckn) != 11:
        return False
    if not tckn.isdigit():
        return False
    if int(tckn[0]) == 0:
        return False

    tckn_sumary = (sum([int(tckn[i]) for i in range(0, 9, 2)]) * 7 - sum([int(tckn[i]) for i in range(1, 9, 2)])) % 10

    if tckn_sumary != int(tckn[9]) or (sum([int(tckn[i]) for i in range(10)]) % 10) != int(tckn[10]):
        return False
    return True
