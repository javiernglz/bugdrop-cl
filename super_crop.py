from PIL import Image
import math

def aggressive_bg_remove_and_crop(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # Sample edges to find the background color
    edge_pixels = []
    for x in range(width):
        edge_pixels.append(pixels[x, 0])
        edge_pixels.append(pixels[x, height-1])
    for y in range(height):
        edge_pixels.append(pixels[0, y])
        edge_pixels.append(pixels[width-1, y])
        
    # Get the most common color on the edges
    from collections import Counter
    bg_color = Counter(edge_pixels).most_common(1)[0][0]
    
    threshold = 50 # Aggressive threshold
    
    min_x = width
    min_y = height
    max_x = 0
    max_y = 0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            
            # Calculate distance
            dist = math.sqrt((r - bg_color[0])**2 + (g - bg_color[1])**2 + (b - bg_color[2])**2)
            
            if dist < threshold:
                pixels[x, y] = (255, 255, 255, 0)
            else:
                # Keep track of bounding box
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x < max_x and min_y < max_y:
        print(f"Cropped to: {min_x}, {min_y}, {max_x}, {max_y}")
        cropped = img.crop((min_x, min_y, max_x, max_y))
        
        # Now make it a perfect square
        cw, ch = cropped.size
        size = max(cw, ch)
        new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
        offset_x = (size - cw) // 2
        offset_y = (size - ch) // 2
        new_img.paste(cropped, (offset_x, offset_y))
        new_img.save(output_path, "PNG")
        print(f"Saved {output_path} with size {size}x{size}")
    else:
        print("Failed to find bounding box.")

source = "/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg"
aggressive_bg_remove_and_crop(source, "frontend-shop/public/logo-head-nobg.png")
aggressive_bg_remove_and_crop(source, "frontend-soc/public/logo-head-nobg.png")
