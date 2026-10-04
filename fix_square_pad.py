from PIL import Image

def make_square_with_padding(input_path, output_path, padding_percent=0.1):
    img = Image.open(input_path).convert("RGBA")
    w, h = img.size
    
    # Calculate the new size with padding
    size = max(w, h)
    pad = int(size * padding_percent)
    new_size = size + (pad * 2)
    
    # Create a new transparent square image
    new_img = Image.new("RGBA", (new_size, new_size), (255, 255, 255, 0))
    
    # Paste the original image into the center
    offset_x = (new_size - w) // 2
    offset_y = (new_size - h) // 2
    new_img.paste(img, (offset_x, offset_y))
    
    new_img.save(output_path, "PNG")

make_square_with_padding("frontend-shop/public/logo-head-nobg.png", "frontend-shop/public/logo-head-nobg.png")
make_square_with_padding("frontend-soc/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png")
