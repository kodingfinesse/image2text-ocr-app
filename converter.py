import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'/home/darren/GitHub/Image2Text/test_image.jpg'

from PIL import Image
import pytesseract

# File path for image
image_path = 'test_image.jpg'

# Use PIL to open image
img = Image.open(image_path)

# Perform OCR on the image with pytesseract
text = pytesseract.image_to_string(img)

# Create and save a text file with same name as image
output_path = image_path.replace('jpg', '.txt')

# Write extracted data to file
with open(output_path, 'w') as file:
    file.write(text)

print(f'Text file has been save to {output_path}')