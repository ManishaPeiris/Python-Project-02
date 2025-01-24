from PIL import Image
import os

image_path = r"C:\Users\manis\BSCS0122011595_A1\BSCS0122011595_A1\cat.jpeg"
img = Image.open(image_path)

compressed_image_path = r"C:\Users\manis\BSCS0122011595_A1\BSCS0122011595_A1\cat_compressed.jpeg"
img.save(compressed_image_path, quality=85, optimize=True)

print(f"Compressed image saved at {compressed_image_path}")
