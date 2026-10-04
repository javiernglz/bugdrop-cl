from PIL import Image

def clean_smart():
    for path in ["frontend-shop/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png"]:
        img = Image.open(path).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        # The right antenna artifact is on the right side of the right antenna.
        # It's lighter than the antenna. The beige head is also light.
        # But the artifact is literally sticking up in the air.
        # We can just erase any pixel that is NOT dark (antenna) in the top right,
        # stopping at Y=50 to not touch the TV head.
        
        for y in range(60):
            for x in range(400, width):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    # If it's bright (artifact), erase it. 
                    # The antenna is dark (r,g,b < 100).
                    if r > 100 and g > 100 and b > 100:
                        pixels[x, y] = (255, 255, 255, 0)
        
        # Do the same for the left antenna just in case
        for y in range(60):
            for x in range(0, 300):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    if r > 100 and g > 100 and b > 100:
                        pixels[x, y] = (255, 255, 255, 0)
                        
        img.save(path, "PNG")

clean_smart()
