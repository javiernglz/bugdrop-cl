from PIL import Image

def chop_antennas(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    head_top = 0
    # Scan from top to bottom
    for y in range(height):
        # Count non-transparent pixels in this row
        row_width = 0
        min_x = width
        max_x = 0
        for x in range(width):
            if pixels[x, y][3] > 0: # If pixel is not fully transparent
                if x < min_x: min_x = x
                if x > max_x: max_x = x
        
        row_width = max_x - min_x if max_x > min_x else 0
        
        # If the row is wider than 60% of the image width, it's the head!
        if row_width > width * 0.6:
            head_top = y
            break
            
    print(f"Antennas end and head starts at Y: {head_top}")
    
    # Crop off the antennas
    cropped_head = img.crop((0, head_top, width, height))
    
    # Get exact bounding box of the new head to be safe
    bbox = cropped_head.getbbox()
    if bbox:
        final_crop = cropped_head.crop(bbox)
        
        # Make perfect square
        cw, ch = final_crop.size
        size = max(cw, ch)
        new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        offset_x = (size - cw) // 2
        offset_y = (size - ch) // 2
        new_img.paste(final_crop, (offset_x, offset_y))
        new_img.save(output_path, "PNG")
        print(f"Saved {output_path} with size {size}x{size}")
    else:
        print("Failed to crop.")

chop_antennas("frontend-shop/public/logo-head-nobg.png", "frontend-shop/public/logo-head-nobg.png")
chop_antennas("frontend-soc/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png")
