from rembg import remove
from PIL import Image
import os

input_path = 'frontend-shop/public/bug-guide-bot.jpg'
output_path = 'frontend-shop/public/bug-guide-nobg.png'
head_path = 'frontend-shop/public/bug-guide-head.png'

# 1. Remove background
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

# 2. Crop head
# The TV head + antennas is around the top center.
cropped = output_image.crop((150, 100, 874, 650))
cropped.save(head_path)
