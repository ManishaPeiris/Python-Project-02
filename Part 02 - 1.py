import cv2
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image_path = r'C:\Users\manis\BSCS0122011595_A1\BSCS0122011595_A1\cat.jpeg'
if not os.path.exists(image_path):
    print(f"Error: File not found at '{image_path}'")
    exit()

img = cv2.imread(image_path)
if img is None:
    print(f"Error: Unable to load image at '{image_path}'")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
if len(faces) == 0:
    print("No faces detected.")
else:
    print(f"Detected faces: {faces}")

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

output_path = r'C:\Users\manis\BSCS0122011595_A1\BSCS0122011595_A1\output.jpg'
cv2.imwrite(output_path, img)
print(f"Output saved at '{output_path}'")
