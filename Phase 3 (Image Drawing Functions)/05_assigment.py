#ask the user  image path and read the image , ask if they want to draw a line, rectangle, circle or text on the image and then ask for the parameters of the shape and draw it on the image and display it
#then ask the value of the parameters for the shape and draw it on the image and display it 
#ask the user if they want to save the image and if yes then ask for the path and save the image

import cv2

image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

if image is None:
    print("Could not read the image.")
else:
    h, w, c = image.shape
    print(f"Image loaded successfully\nHeight: {h}\nWidth: {w}\nChannels: {c}")

    shape = input("Do you want to draw a line, rectangle, circle or text on the image? (line/rectangle/circle/text): ").lower()

    if shape == "line":
        start_point = tuple(map(int, input("Enter the starting point of the line (x,y): ").split(',')))
        end_point = tuple(map(int, input("Enter the ending point of the line (x,y): ").split(',')))
        color = tuple(map(int, input("Enter the color of the line in BGR format (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the line: "))
        cv2.line(image, start_point, end_point, color, thickness)

    elif shape == "rectangle":
        top_left = tuple(map(int, input("Enter the top-left corner of the rectangle (x,y): ").split(',')))
        bottom_right = tuple(map(int, input("Enter the bottom-right corner of the rectangle (x,y): ").split(',')))
        color = tuple(map(int, input("Enter the color of the rectangle in BGR format (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the rectangle border: "))
        cv2.rectangle(image, top_left, bottom_right, color, thickness)

    elif shape == "circle":
        center_coordinates = tuple(map(int, input("Enter the center of the circle (x,y): ").split(',')))
        radius = int(input("Enter the radius of the circle: "))
        color = tuple(map(int, input("Enter the color of the circle in BGR format (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the circle border (-1 for filled circle): "))
        cv2.circle(image, center_coordinates, radius, color, thickness)

    elif shape == "text":
        text = input("Enter the text to be displayed on the image: ")
        position = tuple(map(int, input("Enter the position of the text (x,y): ").split(',')))
        font_scale = float(input("Enter the font scale: "))
        color = tuple(map(int, input("Enter the color of the text in BGR format (B,G,R): ").split(',')))
        thickness = int(input("Enter the thickness of the text: "))
        cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX
                    , font_scale, color, thickness)
        
    else:
        print("Invalid shape choice.")

    cv2.imshow("Image with Shape", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    