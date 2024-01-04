import cv2
import tkinter as tk
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk


def update_image():
    global image

    # Convert the image to PIL format
    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Resize the image to fit the display
    pil_image.thumbnail((400, 400))

    # Convert the PIL image to Tkinter format
    tk_image = ImageTk.PhotoImage(pil_image)

    # Update the image label
    image_label.configure(image=tk_image)
    image_label.image = tk_image


def open_image():
    global image

    # Open a file dialog for image selection
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    # Read the selected image file
    image = cv2.imread(file_path)

    # Update the image display
    update_image()


def crop_image():
    global image

    # Get the crop dimensions from the user
    crop_width = int(crop_width_entry.get())
    crop_height = int(crop_height_entry.get())

    # Crop the image using the user-defined dimensions
    image = image[:crop_height, :crop_width]

    # Update the image display
    update_image()


def resize_image():
    global image

    # Get the resize dimensions from the user
    resize_width = int(resize_width_entry.get())
    resize_height = int(resize_height_entry.get())

    # Resize the image using the user-defined dimensions
    image = cv2.resize(image, (resize_width, resize_height))

    # Update the image display
    update_image()


def adjust_brightness():
    global image

    # Get the brightness value from the user
    brightness = int(brightness_scale.get())

    # Adjust the image brightness using the user-defined value
    image = cv2.add(image, brightness)

    # Update the image display
    update_image()


def adjust_contrast():
    global image

    # Get the contrast value from the user
    contrast = float(contrast_scale.get())

    # Adjust the image contrast using the user-defined value
    image = cv2.multiply(image, contrast)

    # Update the image display
    update_image()


def adjust_sharpness():
    global image

    # Get the sharpness value from the user
    sharpness = float(sharpness_scale.get())

    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1], [-1, sharpness + 9, -1], [-1, -1, -1]])

    # Apply the sharpening kernel to the image
    image = cv2.filter2D(image, -1, kernel)

    # Update the image display
    update_image()


def save_image():
    global image

    # Open a file dialog for saving the modified image
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])

    # Save the image to the specified file path
    cv2.imwrite(file_path, image)


# Create a Tkinter window
window = tk.Tk()
window.title("Image Editor")

# Global variable for the image
image = None

# Create GUI elements
image_label = tk.Label(window)
image_label.pack()

open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

crop_frame = tk.Frame(window)
crop_frame.pack()

crop_label = tk.Label(crop_frame, text="Crop Dimensions:")
crop_label.grid(row=0, column=0, padx=5, pady=5)

crop_width_label = tk.Label(crop_frame, text="Width:")
crop_width_label.grid(row=0, column=1, padx=5, pady=5)
crop_width_entry = tk.Entry(crop_frame)
crop_width_entry.grid(row=0, column=2, padx=5, pady=5)

crop_height_label = tk.Label(crop_frame, text="Height:")
crop_height_label.grid(row=0, column=3, padx=5, pady=5)
crop_height_entry = tk.Entry(crop_frame)
crop_height_entry.grid(row=0, column=4, padx=5, pady=5)

crop_button = tk.Button(crop_frame, text="Crop", command=crop_image)
crop_button.grid(row=0, column=5, padx=5, pady=5)

resize_frame = tk.Frame(window)
resize_frame.pack()

resize_label = tk.Label(resize_frame, text="Resize Dimensions:")
resize_label.grid(row=0, column=0, padx=5, pady=5)

resize_width_label = tk.Label(resize_frame, text="Width:")
resize_width_label.grid(row=0, column=1, padx=5, pady=5)
resize_width_entry = tk.Entry(resize_frame)
resize_width_entry.grid(row=0, column=2, padx=5, pady=5)

resize_height_label = tk.Label(resize_frame, text="Height:")
resize_height_label.grid(row=0, column=3, padx=5, pady=5)
resize_height_entry = tk.Entry(resize_frame)
resize_height_entry.grid(row=0, column=4, padx=5, pady=5)

resize_button = tk.Button(resize_frame, text="Resize", command=resize_image)
resize_button.grid(row=0, column=5, padx=5, pady=5)

brightness_frame = tk.Frame(window)
brightness_frame.pack()

brightness_label = tk.Label(brightness_frame, text="Brightness Adjustment:")
brightness_label.grid(row=0, column=0, padx=5, pady=5)

brightness_scale = tk.Scale(brightness_frame, from_=-255, to=255, orient=tk.HORIZONTAL, length=200)
brightness_scale.grid(row=0, column=1, padx=5, pady=5)

brightness_button = tk.Button(brightness_frame, text="Adjust Brightness", command=adjust_brightness)
brightness_button.grid(row=0, column=2, padx=5, pady=5)

contrast_frame = tk.Frame(window)
contrast_frame.pack()

contrast_label = tk.Label(contrast_frame, text="Contrast Adjustment:")
contrast_label.grid(row=0, column=0, padx=5, pady=5)

contrast_scale = tk.Scale(contrast_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, resolution=0.1, length=200)
contrast_scale.grid(row=0, column=1, padx=5, pady=5)

contrast_button = tk.Button(contrast_frame, text="Adjust Contrast", command=adjust_contrast)
contrast_button.grid(row=0, column=2, padx=5, pady=5)

sharpness_frame = tk.Frame(window)
sharpness_frame.pack()

sharpness_label = tk.Label(sharpness_frame, text="Sharpness Adjustment:")
sharpness_label.grid(row=0, column=0, padx=5, pady=5)

sharpness_scale = tk.Scale(sharpness_frame, from_=0.1, to=2.0, orient=tk.HORIZONTAL, resolution=0.1, length=200)
sharpness_scale.grid(row=0, column=1, padx=5, pady=5)

sharpness_button = tk.Button(sharpness_frame, text="Adjust Sharpness", command=adjust_sharpness)
sharpness_button.grid(row=0, column=2, padx=5, pady=5)

save_button = tk.Button(window, text="Save Image", command=save_image)
save_button.pack()

# Run the Tkinter event loop
window.mainloop()
