import cv2

image = cv2.imread("Phase 2 (Image Resizing & Shaping)/python.png")

if image is None:
    print("Could not read the image.")
else:
    resized_image = cv2.resize(image, (200, 200)) #syntax for resizing an image is cv2.resize(image, (width, height, interpolation)) 
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()