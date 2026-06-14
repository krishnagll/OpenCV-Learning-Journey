"""
Load image (ask the image location from the user)
convert it to grayscale
show that image
save that image with a new name 
(ask if want to save or show the image , if save then ask the name of the image to save)
"""


import cv2

image_path = input("Enter the image path: ")

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    choice = input(
        "Type 'show' to display the grayscale image or 'save' to save it: "
    ).lower()

    if choice == "show":
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == "save":
        file_name = input(
            "Enter file name with extension (e.g., gray_image.jpg): "
        )

        cv2.imwrite(file_name, gray)
        print(f"Image saved as {file_name}")

    else:
        print("Invalid choice!")