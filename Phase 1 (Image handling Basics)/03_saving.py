import cv2 

image = cv2.imread("Phase 1 (Image handling Basics)/python.png")

if image is not None:
    success = cv2.imwrite("Phase 1 (Image handling Basics)/krishna.png", image) # Save the image with a new name
    if success:
        print("image saved successfully.")
    else:
        print("Failed to save the image.")
else:
    print("Image not found.")