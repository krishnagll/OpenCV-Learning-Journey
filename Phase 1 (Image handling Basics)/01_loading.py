import cv2

image = cv2.imread("Phase 1 (Image handling Basics)/python.png")

if image is None:
    print("Image not found.")
else:
    print("Image Loaded successfully.")
    