from rembg import remove
from PIL import Image

input_path = 'frontend-shop/public/bug-ai.jpg'
output_path = 'frontend-shop/public/bug-ai-nobg.png'

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
