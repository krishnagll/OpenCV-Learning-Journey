import cv2

image = cv2.imread("Phase 1 (Image handling Basics)/python.png")
if image is not None:
    h , w , c = image.shape # Get the dimensions of the image (height, width, channels)
    # print("Height:", h)
    # print("Width:", w) 
    # print("Channels:", c)
    print(f"Image loaded succesfully\nHeight:{h}\nWidth:{w}\nChannels:{c}")
else:
    print("Image not found.")
