import cv2
import numpy as np

def main():
    # Get the image path from the user
    image_path = input("Enter the path to the image: ")

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Invalid image file.")
        return

    # Display image dimensions
    height, width, _ = image.shape
    print("Image dimensions: {} x {}".format(width, height))

    while True:
        # Display menu
        print("\n1. Crop")
        print("2. Resize")
        print("3. Adjust Contrast")
        print("4. Adjust Brightness")
        print("5. Adjust Sharpness")
        print("6. Save and Quit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            # Crop image
            x, y, w, h = map(int, input("Enter x, y, width, and height: ").split(","))
            cropped_image = image[y:y+h, x:x+w]
            cv2.imshow("Cropped Image", cropped_image)

        elif choice == 2:
            # Resize image
            new_width, new_height = map(int, input("Enter new width and height: ").split(","))
            resized_image = cv2.resize(image, (new_width, new_height))
            cv2.imshow("Resized Image", resized_image)

        elif choice == 3:
            # Adjust contrast
            alpha = float(input("Enter the contrast factor (1.0-3.0): "))
            adjusted_image = cv2.convertScaleAbs(image, alpha=alpha)
            cv2.imshow("Adjusted Image", adjusted_image)

        elif choice == 4:
            # Adjust brightness
            beta = int(input("Enter the brightness value (-100 to 100): "))
            adjusted_image = cv2.add(image, beta)
            cv2.imshow("Adjusted Image", adjusted_image)

        elif choice == 5:
            # Adjust sharpness
            sigma = float(input("Enter the sigma value (0.1-2.0): "))
            blurred_image = cv2.GaussianBlur(image, (0, 0), sigma)
            sharp_image = cv2.addWeighted(image, 1.5, blurred_image, -0.5, 0)
            cv2.imshow("Sharpened Image", sharp_image)

        elif choice == 6:
            # Save the modified image
            save_path = input("Enter the path to save the modified image: ")
            cv2.imwrite(save_path, image)
            print("Modified image saved successfully.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
