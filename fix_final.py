from PIL import Image

def perfect_square_no_padding(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Crop to exact bounding box first to remove all empty space
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    w, h = img.size
    size = max(w, h)
    
    # Create perfect square
    new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    
    # Paste exactly in center (touches edges on the longest dimension)
    offset_x = (size - w) // 2
    offset_y = (size - h) // 2
    new_img.paste(img, (offset_x, offset_y))
    
    new_img.save(output_path, "PNG")

perfect_square_no_padding("/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg", "frontend-shop/public/logo-head-nobg.png")
perfect_square_no_padding("/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg", "frontend-soc/public/logo-head-nobg.png")
