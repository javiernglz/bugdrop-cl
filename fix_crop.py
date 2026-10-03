from PIL import Image

img = Image.open('frontend-shop/public/bug-guide-nobg.png')
# Full width to avoid cutting the holograms on the right or hand on the left.
cropped = img.crop((0, 50, 1024, 700))
cropped.save('frontend-shop/public/bug-guide-head.png')
