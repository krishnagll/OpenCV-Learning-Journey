import cv2

image = cv2.imread("Phase 1 (Image handling Basics)/python.png")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    cv2.imwrite("Phase 1 (Image handling Basics)/python_gray.png", gray) # Save the grayscale image
else:
    print("Image not found.")