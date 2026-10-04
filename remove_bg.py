from PIL import Image
import sys

def remove_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    new_data = []
    # Get the background color from the top-left pixel
    bg_color = datas[0]
    threshold = 15 # Tolerance for background color
    
    for item in datas:
        # Check if the pixel color is close to the background color
        if abs(item[0] - bg_color[0]) < threshold and \
           abs(item[1] - bg_color[1]) < threshold and \
           abs(item[2] - bg_color[2]) < threshold:
            new_data.append((255, 255, 255, 0)) # Transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

remove_background("/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg", "logo-head-nobg.png")
