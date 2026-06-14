import cv2

image = cv2.imread("Phase 2 (Image Resizing & Shaping)/python.png")

if image is None:
    print("Image not found")
    
else:
    ( h , w ) = image.shape[:2] #:2 is used to ignore the channels and get only height and width
    
    center = ( w//2 , h//2 )

    M = cv2.getRotationMatrix2D(center, 45, 1.0) #syntax for rotation is cv2.getRotationMatrix2D(center, angle, scale)
    rotated_image = cv2.warpAffine(image, M, (w, h)) #syntax for applying the rotation is cv2.warpAffine(image, M, (width, height))

    cv2.imshow("Rotated Image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()