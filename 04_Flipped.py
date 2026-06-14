import cv2

image = cv2.imread("Phase 2 (Image Resizing & Shaping)/python.png")

if image is None:
    print("Could not read the image.")
else:
    Flipped_horizontal = cv2.flip(image, 1) #syntax for horizontal flip is cv2.flip(image, 1)
    Flipped_vertical = cv2.flip(image, 0) #syntax for vertical flip is cv2.flip(image, 0)
    Flipped_Both = cv2.flip(image, -1) #syntax for both horizontal and vertical flip is cv2.flip(image, -1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Flipped Horizontal", Flipped_horizontal)
    cv2.imshow("Flipped Vertical", Flipped_vertical)
    cv2.imshow("Flipped Both", Flipped_Both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()