from PIL import Image

def make_square(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    
    # Make it a square using the largest dimension
    size = max(w, h)
    
    # Create a new transparent square image
    new_img = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    
    # Paste the original image into the center
    offset_x = (size - w) // 2
    offset_y = (size - h) // 2
    new_img.paste(img, (offset_x, offset_y))
    
    new_img.save(output_path, "PNG")

make_square("frontend-shop/public/logo-head-nobg.png", "frontend-shop/public/logo-head-nobg.png")
make_square("frontend-soc/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png")
