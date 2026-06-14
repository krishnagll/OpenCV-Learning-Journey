import cv2

image = cv2.imread("Phase 2 (Image Resizing & Shaping)/python.png")

if image is None:
    print("Could not read the image.")
else:
    Cropped_image = image[200:1000 , 200:1000] #syntax for cropping an image is image[y1:y2, x1:x2]
    cv2.imshow("Original Image", image)
    cv2.imshow("Cropped Image", Cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()