import csv
from os.path import join
import xml.etree.ElementTree as ET

import os

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    os.system(("pip" if os.name == "nt" else "pip3") +
              " install -r requirements.txt && " +
              ("cls" if os.name == "nt" else "clear"))

from PIL import Image, ImageDraw, ImageFont


def utf_to_png(utf_char, output_file, font_size=96):
    image = Image.new('RGB', (128, 128), color='white')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("japenese.otf", font_size)

    text_width = draw.textlength(utf_char, font=font)
    x = (128 - text_width) / 2
    y = -10

    draw.text((x, y), utf_char, fill='black', font=font)

    image.save(output_file)


if __name__ == '__main__':
    root = ET.parse("data.xml").getroot()
    csv_filename = 'extracted_data.csv'
    out = open(csv_filename, 'w')
    csv_writer = csv.writer(out)
    csv_writer.writerow(['ID', 'literal', 'Meanings', 'link'])
    count = 0
    characters = root.findall('.//character')

    for char in characters:
        literal = char.find('.//literal').text
        meanings = [meaning.text for meaning in char.findall('.//meaning') if len(meaning.attrib) == 0]
        csv_writer.writerow([count, literal, meanings, f"=HYPERLINK(\"file:///{join(os.getcwd(), 'images', str(count)+'.png')}\", \"See {count}.png\")"])
        utf_to_png(literal, f'images/{count}.png')
        count += 1
        print(f"Extracted data written to {csv_filename}")
