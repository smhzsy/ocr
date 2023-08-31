import re

from config import patterns
from converter import convert_date
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
    seen_values = []
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text, re.MULTILINE)

        if label == "PHONE_NUMBER":
            valid_nums = []
            for number in matches:
                if IsValidNumber(str(number)) and number not in seen_values:
                    valid_nums.append({"value": number, "type": "PHONE_NUMBER"})
                    seen_values.append(number)
            matches = valid_nums

        if label == "PHONE_NUMBER2":
            valid_nums = []
            for number in matches:
                if number not in seen_values:
                    valid_nums.append({"value": number, "type": "PHONE_NUMBER"})
                    seen_values.append(number)
            matches = valid_nums

        if label == "ID":
            valid_tckns = []
            for tckn in matches:
                if IsValidID(tckn) and tckn not in seen_values:
                    valid_tckns.append({"value": tckn, "type": "ID"})
                    seen_values.append(tckn)
            matches = valid_tckns

        if label == "CREDIT_CARD":
            valid_cards = []
            for card in matches:
                if luhn_check(card) and card not in seen_values:
                    valid_cards.append({"value": card, "type": "CREDIT_CARD"})
                    seen_values.append(card)
            matches = valid_cards

        if label == "PLATE":
            valid_plates = []
            for plate in matches:
                if IsValidPlate(plate) and plate not in seen_values:
                    valid_plates.append({"value": plate, "type": "PLATE"})
                    seen_values.append(plate)
            matches = valid_plates

        if label == "DATETIME":
            valid_dates = []
            for date in matches:
                converted_date = convert_date(date)
                if convert_date(date) and date not in seen_values:
                    valid_dates.append({"value": converted_date, "type": "DATE"})
                    seen_values.append(date)
            matches = valid_dates

        if label == "E-MAIL":
            valid_mails = []
            for mail in matches:
                if mail not in seen_values:
                    valid_mails.append({"value": mail, "type": "EMAIL"})
                    seen_values.append(mail)
            matches = valid_mails

        if label == "DOMAIN":
            valid_domains = []
            for domain in matches:
                if domain not in seen_values:
                    valid_domains.append({"value": domain, "type": "DOMAIN"})
                    seen_values.append(domain)
            matches = valid_domains

        if label == "URL":
            valid_urls = []
            for url in matches:
                if url not in seen_values:
                    valid_urls.append({"value": url, "type": "URL"})
                    seen_values.append(url)
            matches = valid_urls

        if label == "MD5-HASH" or label == "SHA1-HASH" or label == "SHA256-HASH":
            valid_hash = []
            for hash in matches:
                if hash not in seen_values:
                    valid_hash.append({"value": hash, "type": "HASH"})
                    seen_values.append(hash)
            matches = valid_hash

        if label == "COMBOLIST":
            valid_combolist = []
            for combo in matches:
                if combo not in seen_values:
                    valid_combolist.append({"value": combo, "type": "COMBOLIST"})
                    seen_values.append(combo)
            matches = valid_combolist

        if matches:
            results.extend(matches)

    response = {
        "content": text,
        "status": "successful",
        "findings": results
    }

    return response
