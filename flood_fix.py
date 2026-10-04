from PIL import Image, ImageDraw

def process_perfect_logo():
    # 1. Open original generated JPG
    input_path = "/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg"
    img = Image.open(input_path).convert("RGBA")
    
    # 2. Floodfill to remove only outer background
    ImageDraw.floodfill(img, (0, 0), (255, 255, 255, 0), thresh=40)
    
    # 3. Get the bounding box of the now transparent-background image
    bbox = img.getbbox()
    img = img.crop(bbox)
    
    # 4. Chop antennas
    width, height = img.size
    pixels = img.load()
    
    head_top_y = 0
    for y in range(height):
        # Count actual solid pixels in this row
        solid_pixels = sum(1 for x in range(width) if pixels[x, y][3] > 0)
        
        # The main TV body is solid. If more than 40% of the width is solid pixels, it's the head!
        if solid_pixels > width * 0.4:
            head_top_y = y
            break
            
    print(f"Chopping antennas at Y: {head_top_y}")
    
    # Chop off antennas
    img = img.crop((0, head_top_y, width, height))
    
    # Find new bounding box just in case
    bbox2 = img.getbbox()
    img = img.crop(bbox2)
    
    # Make a perfect square
    w, h = img.size
    size = max(w, h)
    final_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    
    offset_x = (size - w) // 2
    offset_y = (size - h) // 2
    final_img.paste(img, (offset_x, offset_y))
    
    output1 = "frontend-shop/public/logo-head-nobg.png"
    output2 = "frontend-soc/public/logo-head-nobg.png"
    final_img.save(output1, "PNG")
    final_img.save(output2, "PNG")
    print(f"Success! Final size: {size}x{size}")

process_perfect_logo()
