from PIL import Image, ImageDraw

def restore_properly():
    input_path = "/Users/javiglz/.gemini/antigravity/brain/a8f16413-7459-4d9a-8d53-8ed6db4f6394/bug_head_favicon_1791141181441.jpg"
    img = Image.open(input_path).convert("RGBA")
    
    # 1. Floodfill with VERY LOW threshold to not eat the antennas
    # Let's check top-left pixel color
    pixels = img.load()
    bg_color = pixels[0, 0]
    print("Background color is:", bg_color)
    
    # Threshold 15 is usually safe for compression noise on flat backgrounds
    ImageDraw.floodfill(img, (0, 0), (255, 255, 255, 0), thresh=10)
    
    # Let's also floodfill from top-right just in case
    ImageDraw.floodfill(img, (img.size[0]-1, 0), (255, 255, 255, 0), thresh=10)
    
    # 2. Hardcoded perfect square crop
    # Based on the known bbox of the TV head (165, 74, 859, 890)
    img = img.crop((165, 196, 859, 890))
    
    output1 = "frontend-shop/public/logo-head-nobg.png"
    output2 = "frontend-soc/public/logo-head-nobg.png"
    img.save(output1, "PNG")
    img.save(output2, "PNG")
    print(f"Restored and saved carefully! Size: {img.size}")

restore_properly()
