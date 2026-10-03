from rembg import remove
from PIL import Image

input_path = 'frontend-shop/public/bug-guide-bot.jpg'
output_path = 'frontend-shop/public/bug-guide-nobg.png'
head_path = 'frontend-shop/public/bug-guide-head.png'

# 1. Remove background
input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)

# 2. Crop head. Let's make it a nice square or 4:3 box focused on the head and hand.
# Center of face is ~512. Hand is on the left.
cropped = output_image.crop((150, 80, 850, 650))
cropped.save(head_path)
