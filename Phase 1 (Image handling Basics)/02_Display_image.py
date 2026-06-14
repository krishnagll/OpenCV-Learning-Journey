import cv2

image = cv2.imread("Phase 1 (Image handling Basics)/python.png")

if image is not None :
    cv2.imshow("Image loaded successfully", image) # Display the image in a window
    cv2.waitKey(0) # Wait for a key press to close the window
    cv2.destroyAllWindows() # Close all OpenCV windows
else:
    print("Image not found.")
