import cv2

image = cv2.imread("Phase 3 (Image Drawing Functions)/python.png")

if image is None:
    print("Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image loaded successfully\nHeight: {h}\nWidth: {w}\nChannels: {c}")

    cv2.putText(image, "OpenCV", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
#syntax for putting text on image is cv2.putText(image, text, position, font, font_scale, color, thickness)
    cv2.imshow("Image with Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()