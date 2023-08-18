import re

from config import patterns
from validators.credit_card_validator import luhn_check
from validators.id_validator import IsValidID
from validators.number_validator import IsValidNumber
from validators.plate_validator import IsValidPlate


def find_credentials(text: str) -> dict:
    """
    Analyzing the text with regex's and categorizing them.
    :param text: Text to analyze.
    :return: Dict
    """

    results = []

    for label, pattern in patterns.items():
        matches = re.findall(pattern, text, re.MULTILINE)

        if label == "PHONE_NUMBER":
            valid_nums = []
            for number in matches:
                if IsValidNumber(str(number)):
                    valid_nums.append({"value": number, "type": "PHONE_NUMBER"})
            matches = valid_nums

        if label == "ID":
            valid_tckns = []
            for tckn in matches:
                if IsValidID(tckn):
                    valid_tckns.append({"value": tckn, "type": "ID"})
            matches = valid_tckns

        if label == "CREDIT_CARD":
            valid_cards = []
            for card in matches:
                if luhn_check(card):
                    valid_cards.append({"value": card, "type": "CREDIT_CARD"})
            matches = valid_cards

        if label == "PLATE":
            valid_plates = []
            for plate in matches:
                if IsValidPlate(plate):
                    valid_plates.append({"value": plate, "type": "PLATE"})
            matches = valid_plates

        if label == "DATETIME":
            valid_dates = []
            for date in matches:
                valid_dates.append({"value": date, "type": "DATETIME"})
            matches = valid_dates

        if label == "E-MAIL":
            valid_mails = []
            for mail in matches:
                valid_mails.append({"value": mail, "type": "E-MAIL"})
            matches = valid_mails

        if label == "DOMAIN":
            valid_domains = []
            for domain in matches:
                valid_domains.append({"value": domain, "type": "DOMAIN"})
            matches = valid_domains

        if label == "URL":
            valid_urls = []
            for url in matches:
                valid_urls.append({"value": url, "type": "URL"})
            matches = valid_urls

        if label == "MD5-HASH":
            valid_mdhash = []
            for hash in matches:
                valid_mdhash.append({"value": hash, "type": "MD5-HASH"})
            matches = valid_mdhash

        if label == "SHA1-HASH":
            valid_s1hash = []
            for hash in matches:
                valid_s1hash.append({"value": hash, "type": "SHA1-HASH"})
            matches = valid_s1hash

        if label == "SHA256-HASH":
            valid_s256hash = []
            for hash in matches:
                valid_s256hash.append({"value": hash, "type": "SHA256-HASH"})
            matches = valid_s256hash

        if label == "COMBOLIST":
            valid_combolist = []
            for combo in matches:
                valid_combolist.append({"value": combo, "type": "COMBOLIST"})
            matches = valid_combolist

        if matches:
            results.extend(matches)

    response = {
        "content": text,
        "status": "successful",
        "findings": results
    }

    return response
