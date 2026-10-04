from PIL import Image, ImageDraw

def process_manual():
    input_path = "/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg"
    img = Image.open(input_path).convert("RGBA")
    
    # 1. Floodfill to remove outer background
    ImageDraw.floodfill(img, (0, 0), (255, 255, 255, 0), thresh=40)
    
    # 2. Hardcoded perfect square crop
    # Based on the known bbox of the TV head (165, 74, 859, 890)
    # Width is 859 - 165 = 694
    # Height should be 694, anchored at the bottom (890)
    # Top Y = 890 - 694 = 196
    
    img = img.crop((165, 196, 859, 890))
    
    # Save
    output1 = "frontend-shop/public/logo-head-nobg.png"
    output2 = "frontend-soc/public/logo-head-nobg.png"
    img.save(output1, "PNG")
    img.save(output2, "PNG")
    print(f"Success! Final size: {img.size}")

process_manual()
