from PIL import Image

def crop_to_content(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    # Get the bounding box of the non-transparent alpha channel
    bbox = img.getbbox()
    if bbox:
        img_cropped = img.crop(bbox)
        img_cropped.save(output_path, "PNG")
        print("Cropped successfully to bounding box:", bbox)
    else:
        print("Empty image, could not crop")

crop_to_content("frontend-shop/public/logo-head-nobg.png", "frontend-shop/public/logo-head-nobg.png")
crop_to_content("frontend-soc/public/logo-head-nobg.png", "frontend-soc/public/logo-head-nobg.png")
