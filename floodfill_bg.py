from PIL import Image

def remove_bg():
    img = Image.open('frontend-shop/public/bug-ai.jpg').convert('RGBA')
    width, height = img.size
    
    # We want to keep only the center area.
    # We will do a basic floodfill from the corners (0,0), (width-1, 0), (0, height-1), (width-1, height-1)
    # matching the background color with some tolerance.
    
    # Actually, a much easier trick:
    # Just grab all pixels that are very close to white/grey.
    
    data = img.getdata()
    new_data = []
    for r, g, b, a in data:
        # The background is a gradient of whites/greys.
        # If it's bright enough and has low saturation (r, g, b are close to each other), it's background.
        # The AI suit has some neon blue (so B is high, R is low) which we want to keep.
        # The suit is white, but has lines.
        # Let's just rely on rembg.
        pass

