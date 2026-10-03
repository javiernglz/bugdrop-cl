from PIL import Image
img = Image.open('frontend-shop/public/bug-ai-nobg.png')
# Original size is 1024x1024
# The head is roughly in the top middle.
# Let's crop from (x1=250, y1=100) to (x2=774, y2=550) - this is a 524x450 box.
cropped = img.crop((200, 100, 824, 600))
cropped.save('frontend-shop/public/bug-ai-head.png')
