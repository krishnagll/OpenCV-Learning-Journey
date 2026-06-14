import cv2

image = cv2.imread("Phase 3 (Image Drawing Functions)/python.png")

if image is None:
    print("Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image loaded successfully\nHeight: {h}\nWidth: {w}\nChannels: {c}")

    # Draw a line on the image
    start_point = (50, 50)  # Starting point of the line
    end_point = (100, 100)  # Ending point of the line

    color = (0, 255, 0)  # Color of the line in BGR (Green)
    thickness = 5  # Thickness of the line

    cv2.line(image, start_point, end_point, color, thickness)

    # Display the image with the drawn line
    cv2.imshow("Image with Line", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()