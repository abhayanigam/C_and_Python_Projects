from pdf2image import convert_from_path
import os

# Directory to save the images
output_dir = '/home/1team009/Desktop/practice/Problems/OCR_File/images'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Path to the PDF file
pdf_path = 'example.pdf'

# Convert each page of the PDF file to an image
images = convert_from_path(pdf_path)

# Save each image to the output directory
for i, image in enumerate(images):
    image_path = os.path.join(output_dir, f'page{i}.jpg')
    image.save(image_path, 'JPEG')
    print(f'Image saved: {image_path}')






# # Import library
# import PyPDF2

# # Open the PDF file in binary mode
# # with open("sample.pdf", "rb") as pdf_file:
# with open("example2.pdf", "rb") as pdf_file:
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
    
#     num_pages = len(pdf_reader.pages)
    
#     first_page = pdf_reader.pages[0]
    
#     text = first_page.extract_text()
    
#     print("Number of Pages:", num_pages)
#     print("Text:\n" + text)
