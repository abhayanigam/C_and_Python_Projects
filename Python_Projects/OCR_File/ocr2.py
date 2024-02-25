# import pytesseract
# from PIL import Image

# # Path to the image file
# image_path = '/home/1team009/Desktop/practice/Problems/OCR_File/images/page0.jpg'

# # Open the image using PIL (Python Imaging Library)
# img = Image.open(image_path)

# # Perform OCR on the image using pytesseract
# text = pytesseract.image_to_string(img)

# # Print the extracted text
# print(text)







from pdf2image import convert_from_path
import os
import pytesseract
from PIL import Image

# Directory to save the images
output_dir = '/home/1team009/Desktop/practice/Problems/OCR_File/images'

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

# Save each image to the output directory
for i, image in enumerate(images):
    image_path = os.path.join(output_dir, f'page{i}.jpg')
    image.save(image_path, 'JPEG')
    print(f'Image saved: {image_path}')

# Perform OCR on the first image (page0.jpg)
image_path = os.path.join(output_dir, 'page0.jpg')
if not os.path.exists(image_path):
    print(f"Error: {image_path} not found")
    exit()

# Open the image using PIL (Python Imaging Library)
img = Image.open(image_path)

# Perform OCR on the image using pytesseract
text = pytesseract.image_to_string(img, lang='eng', config='--psm 6')

# Print the extracted text
print(text)
