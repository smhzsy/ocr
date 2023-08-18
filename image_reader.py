import pytesseract
from PIL import Image


def read_text_from_img(image_path: str) -> str:
    """
    Reading the text from image.
    :param image_path: The path of the image.
    :return: String
    """
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return str(e)
