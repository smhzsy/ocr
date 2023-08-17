import re

from validators.credit_card_validator import luhn_check
from validators.id_validator import IsValidID
from validators.number_validator import IsValidNumber
from validators.plate_validator import IsValidPlate


def veri_bul(text):
    patterns = {
        "Telefon Numaraları": r'(?:\+90.?5|0090.?5|905|0?5)(?:[01345][0-9])\s?(?:[0-9]{3})\s?(?:[0-9]{2})\s?(?:[0-9]{2})',
        "Kimlik Numaraları": r'\b[1-9]{1}[0-9]{9}[02468]{1}',
        "Kredi Kartı Numaraları": r'\b(?:\d{4}[ -]?){3}\d{4}\b',
        "Plakalar": r"\b\d{2} [A-Z]{1,3} \d{2,4}\b|\b\d{2} [A-Z]{2} \d{3}\b|\b\d{2} [A-Z]{3} \d{2,3}\b|\b\d{2}[A-Z]{3}\d{2}\b|\b\d{2}[A-Z]{2}\d{3}\b|\b\d{2}[A-Z]{1,3}\d{2,4}\b",
        "Tarihler": r'\b\d{2}[/\.]\d{2}[/\.]\d{4}\b',
        "E-posta Adresleri": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        "Alan Adları": r'\b(?:https?://)?([A-Za-z_0-9.-]+(?:\.[A-Za-z]{2,})+)\b',
        "URL'ler": r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        "md Hash Değerleri": r'\b[a-fA-F0-9]{32}\b',
        "s1 Hash Değerleri": r'\b[a-fA-F0-9]{40}\b',
        "s256 Hash Değerleri": r'\b[a-fA-F0-9]{64}\b',
        "Combolist Verileri": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+[*:][^\s]+',
    }

    results = []

    for label, pattern in patterns.items():
        matches = re.findall(pattern, text, re.MULTILINE)

        if label == "Telefon Numaraları":
            valid_nums = []
            for number in matches:
                if IsValidNumber(str(number)):
                    valid_nums.append({"value": number, "type": "PHONE_NUMBER"})
            matches = valid_nums

        if label == "Kimlik Numaraları":
            valid_tckns = []
            for tckn in matches:
                if IsValidID(tckn):
                    valid_tckns.append({"value": tckn, "type": "ID"})
            matches = valid_tckns

        if label == "Kredi Kartı Numaraları":
            valid_cards = []
            for card in matches:
                if luhn_check(card):
                    valid_cards.append({"value": card, "type": "CREDIT_CARD"})
            matches = valid_cards

        if label == "Plakalar":
            valid_plates = []
            for plate in matches:
                if IsValidPlate(plate):
                    valid_plates.append({"value": plate, "type": "PLATE"})
            matches = valid_plates

        if label == "Tarihler":
            valid_dates = []
            for date in matches:
                valid_dates.append({"value": date, "type": "DATETIME"})
            matches = valid_dates

        if label == "E-posta Adresleri":
            valid_mails = []
            for mail in matches:
                valid_mails.append({"value": mail, "type": "E-MAIL"})
            matches = valid_mails

        if label == "Alan Adları":
            valid_domains = []
            for domain in matches:
                valid_domains.append({"value": domain, "type": "DOMAIN"})
            matches = valid_domains

        if label == "URL'ler":
            valid_urls = []
            for url in matches:
                valid_urls.append({"value": url, "type": "URL"})
            matches = valid_urls

        if label == "md Hash Değerleri":
            valid_mdhash = []
            for hash in matches:
                valid_mdhash.append({"value": hash, "type": "MD5-HASH"})
            matches = valid_mdhash

        if label == "s1 Hash Değerleri":
            valid_s1hash = []
            for hash in matches:
                valid_s1hash.append({"value": hash, "type": "SHA1-HASH"})
            matches = valid_s1hash

        if label == "s256 Hash Değerleri":
            valid_s256hash = []
            for hash in matches:
                valid_s256hash.append({"value": hash, "type": "SHA256-HASH"})
            matches = valid_s256hash

        if label == "Combolist Verileri":
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
