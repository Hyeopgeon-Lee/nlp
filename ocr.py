from PIL import Image
from pytesseract import *

image = Image.open("sample.jpg")

print01 = image_to_string(image, lang='eng')

print(print01)