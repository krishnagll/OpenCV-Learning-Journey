import cv2

image = cv2.imread("Phase 3 (Image Drawing Functions)/python.png")

if image is None:
    print("Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image loaded successfully\nHeight: {h}\nWidth: {w}\nChannels: {c}")

    # Draw a rectangle on the image
    top_left = (50, 50)  # Top-left corner of the rectangle
    bottom_right = (200, 200)  # Bottom-right corner of the rectangle
    color = (0, 0, 255)  # Color of the rectangle in BGR (Red)
    thickness = 5  # Thickness of the rectangle border

    cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # Display the image with the drawn rectangle
    cv2.imshow("Image with Rectangle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()