import csv


def check_db(value: str) -> bool:
    """
    Checks example company employee database. Returns True if found.
    :param value: Value found in OCR.
    :return: bool
    """
    csvdosya = "employees.csv"
    try:
        with open(csvdosya, 'r', newline='', encoding='utf-8') as dosya:
            csv_okuyucu = csv.reader(dosya)
            found_lines = []

            for satir in csv_okuyucu:
                if value in satir:
                    found_lines.append(satir)

            if found_lines:
                for satir in found_lines:
                    return True
            else:
                return False

    except FileNotFoundError:
        return False