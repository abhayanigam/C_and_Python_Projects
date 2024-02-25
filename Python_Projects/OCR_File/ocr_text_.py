from pdf2image import convert_from_path
import os
import pytesseract
from PIL import Image
import re

# Directory to save the images
output_dir = '/home/1team009/Desktop/practice/Problems/OCR_File/images'


def extract_name(text):
    pattern = r"\sName\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_mothers_name(text):
    pattern = r"Mothers Name\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_fathers_name(text):
    pattern = r"Fathers Name\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_husbands_name(text):
    pattern = r"Husband's Name\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_house_number(text):
    pattern = r"House Number\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_age(text):
    pattern = r"Age\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""

def extract_gender(text):
    pattern = r"Gender\s*:\s*(.*)"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return ""


# Create the output directory if it doesn't exist
try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as e:
    print(f"Error: {output_dir} - {e.strerror}")
    exit()

# Path to the PDF file
pdf_path = 'example.pdf'

# Convert each page of the PDF file to an image
images = convert_from_path(pdf_path)

# Initialize an empty string to store all extracted text
all_text = ''

# Iterate over each image and perform OCR
for i in range(len(images)):
    image_path = os.path.join(output_dir, f'page{i}.jpg')
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found")
        continue

    # Open the image using PIL (Python Imaging Library)
    img = Image.open(image_path)

    # Perform OCR on the image using pytesseract
    text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')

    # Split the text into lines and process each line
    for line in text.split('\n'):
        if not any(keyword in line for keyword in ["Assembly Constituency No and Name", "Section No and Name"]):
            name = extract_name(line)
            mothers_name = extract_mothers_name(line)
            fathers_name = extract_fathers_name(line)
            husbands_name = extract_husbands_name(line)
            house_number = extract_house_number(line)
            age = extract_age(line)
            gender = extract_gender(line)

            # Format the entire line with extracted attributes
            formatted_line = f"Name : {name}\n" \
                             f"Mothers Name: {mothers_name}\n" \
                             f"Fathers Name: {fathers_name}\n" \
                             f"Husbands Name: {husbands_name}\n" \
                             f"House Number: {house_number}\n" \
                             f"Age: {age}\n" \
                             f"Gender: {gender}\n\n"

            # Append the formatted line to the all_text string
            all_text += formatted_line

# Save all extracted text to a single file
text_file_path = os.path.join('/home/1team009/Desktop/practice/Problems/OCR_File/textfiles', 'all_text.txt')
with open(text_file_path, 'w') as f:
    f.write(all_text)

print(f'All text saved to: {text_file_path}')