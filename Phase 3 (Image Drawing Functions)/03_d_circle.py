import cv2

image = cv2.imread("Phase 3 (Image Drawing Functions)/python.png")

if image is None:
    print("Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image loaded successfully\nHeight: {h}\nWidth: {w}\nChannels: {c}")

    # Draw a circle on the image
    center_coordinates = (150, 150)  # Center of the circle
    radius = 50  # Radius of the circle
    color = (255, 0, 0)  # Color of the circle in BGR (Blue)
    thickness = 7  # Thickness of the circle border (-1 for filled circle)

    cv2.circle(image, center_coordinates, radius, color, thickness)

    # Display the image with the drawn circle
    cv2.imshow("Image with Circle", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()