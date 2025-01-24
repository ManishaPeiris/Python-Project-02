from PIL import Image
import matplotlib.pyplot as plt

image= "cat.jpeg"
try:
    img = Image.open(image)
    print(f"Image loaded successfully: {img.format}, {img.size}, {img.mode}")

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

except FileNotFoundError:
    print(f"Error: The file at '{image}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
