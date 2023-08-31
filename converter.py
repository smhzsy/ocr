from dateutil.parser import parse


def convert_date(date_str: str):
    try:
        output_format = "%Y-%m-%d %H:%M:%S"
        date = parse(date_str)
        output_date_str = date.strftime(output_format)
        return output_date_str
    except Exception as e:
        return False
