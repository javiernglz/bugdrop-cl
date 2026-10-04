from PIL import Image

def clean():
    for path in ["frontend-shop/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png"]:
        img = Image.open(path).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        # Clean white/grey artifacts in the top portion (antennas)
        for y in range(250):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if a > 0:
                    # If it's a light grey/white color (the background residue)
                    # The antennas themselves are dark brown/black.
                    if r > 160 and g > 160 and b > 160:
                        pixels[x, y] = (255, 255, 255, 0)
        img.save(path, "PNG")

clean()
