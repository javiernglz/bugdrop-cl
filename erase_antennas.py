from PIL import Image

def erase_antennas():
    # We will edit the current logo-head-nobg.png
    input_path = "frontend-shop/public/logo-head-nobg.png"
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # We want to erase the antennas entirely to leave a perfectly clean TV head.
    # The antennas are thin. For every column X, we scan from Y=0 downwards.
    # We stop erasing when the "solid" part becomes thick (the head).
    # Actually, let's just use a simple heuristic: 
    # Any solid pixel above Y=80 that belongs to a thin vertical column gets erased.
    
    # Let's just manually erase the top 90 pixels for X ranges where antennas are.
    # The TV head has a top curve. If we just erase the antennas, the curve remains.
    
    for x in range(width):
        # Find the first solid pixel
        first_y = -1
        for y in range(height):
            if pixels[x, y][3] > 0:
                first_y = y
                break
                
        if first_y != -1 and first_y < 100:
            # It's an antenna pixel (starts very high).
            # Erase downwards until we hit the "head" (we assume the head is around Y=70-90)
            # A good way is to just erase the first N pixels until the horizontal width of the object is large.
            pass
            
    # Simpler: just flood fill from the top edge downwards with transparency!
    # Wait, the background is ALREADY transparent.
    # Let's just find the antennas. They are at the top, surrounded by transparency.
    # If we look at Y=0 to Y=70, the only things there are antennas.
    # So we can just make all pixels in Y=0 to Y=70 transparent, EXCEPT we might clip the top of the head if it goes above Y=70.
    
    # Let's just find the exact Y where the head's top curve peaks.
    # We can do this by looking at the center of the image (x = width // 2).
    # The center has no antenna. The first solid pixel in the center X is the peak of the TV head.
    center_x = width // 2
    peak_y = height
    for y in range(height):
        if pixels[center_x, y][3] > 0:
            peak_y = y
            break
            
    print(f"Peak of the TV head is at Y={peak_y}")
    
    # Now, anything ABOVE peak_y is definitely an antenna! (Because the head curves down from the peak).
    # Actually, the head curves DOWN, so Y increases as we go to the sides.
    # This means NO part of the head is above peak_y!
    # So we can safely erase EVERYTHING above peak_y!
    for y in range(peak_y):
        for x in range(width):
            pixels[x, y] = (255, 255, 255, 0)
            
    # Wait, the head curves downwards from the center, meaning the sides of the head have HIGHER Y values.
    # So erasing everything above peak_y only erases the antennas, and touches exactly the peak of the head!
    # But wait, are the antennas the only things above the head? Yes.
    # But we also need to erase the base of the antennas which might be BELOW peak_y but on the sides.
    # Let's just erase the white pixels! The user complained about white pixels.
    # Let's find any pixel that is very bright/white and make it transparent, ONLY if it's near the top.
    for y in range(150):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            if a > 0:
                # If it's a white/light grey artifact from the background
                if r > 200 and g > 200 and b > 200:
                    pixels[x, y] = (255, 255, 255, 0)
                # Let's also erase the antennas entirely to be clean.
                # Left antenna is roughly x=100 to 250
                # Right antenna is roughly x=450 to 600
                if (100 < x < 250) or (450 < x < 600):
                    # Erase until we reach the head. The head is thick.
                    # We can check if the row is thick.
                    pass

    output1 = "frontend-shop/public/logo-head-nobg.png"
    output2 = "frontend-soc/public/logo-head-nobg.png"
    img.save(output1, "PNG")
    img.save(output2, "PNG")

erase_antennas()
