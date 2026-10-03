from rembg import remove
from PIL import Image

input_path = 'frontend-shop/public/bug-rules.jpg'
output_path = 'frontend-shop/public/bug-rules-nobg.png'
head_path = 'frontend-shop/public/bug-rules-head.png'

# 1. Remove background
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

# 2. Crop head. Let's include the gavel on the left.
# Center of face is ~512. Hand with gavel is on the left.
cropped = output_image.crop((180, 80, 850, 600))
cropped.save(head_path)
