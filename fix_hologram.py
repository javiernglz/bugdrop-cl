from PIL import Image

img = Image.open('frontend-shop/public/bug-guide-bot.jpg').convert("RGBA")
nobg = Image.open('frontend-shop/public/bug-guide-nobg.png').convert("RGBA")

# Let's inspect a pixel in the top left of the original image to get the exact background color
bg_pixel = img.getpixel((10, 10))
print("Background color is:", bg_pixel)

