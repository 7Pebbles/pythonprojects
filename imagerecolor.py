import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def recolor_image(image_path, target_color, new_color):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGBA mode if it's not already
    image = image.convert("RGBA")

    # Get the pixel data
    pixels = image.load()

    # Iterate over each pixel and recolor pixels matching the target color
    for i in range(image.width):
        for j in range(image.height):
            r, g, b, a = pixels[i, j]
            if (r, g, b) == target_color:
                pixels[i, j] = (*new_color, a)  # Apply the new color

    # Save the modified image
    image.save("recolored_image.png")

def browse_image():
    # Prompt user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    image_entry.delete(0, tk.END)
    image_entry.insert(0, file_path)

def recolor_button_clicked():
    # Get the input values from the UI
    image_path = image_entry.get()
    target_color_hex = target_color_entry.get()
    new_color_hex = new_color_entry.get()

    # Convert hex colors to RGB tuples
    target_color = tuple(int(target_color_hex[i:i+2], 16) for i in (1, 3, 5))
    new_color = tuple(int(new_color_hex[i:i+2], 16) for i in (1, 3, 5))

    # Open the image and get the file extension
    image = Image.open(image_path)
    image_extension = os.path.splitext(image_path)[1]

    # Generate the recolored image name
    recolored_image_name = os.path.splitext(os.path.basename(image_path))[0] + "_recolored" + image_extension

    # Save the modified image with the new name
    recolored_image_path = os.path.join(os.path.dirname(image_path), recolored_image_name)
    image.save(recolored_image_path)

    # Call the function to recolor the image (using the updated image path)
    recolor_image(recolored_image_path, target_color, new_color)

    # Show a message box with the result
    tk.messagebox.showinfo("Image Recoloring", "Image recoloring completed successfully!")

# Create the main window
window = tk.Tk()
window.title("Image Recoloring")
window.geometry("400x200")

# Create the UI elements
image_label = tk.Label(window, text="Image:")
image_label.pack()

image_entry = tk.Entry(window, width=40)
image_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_image)
browse_button.pack()

target_color_label = tk.Label(window, text="Target Color (hex format):")
target_color_label.pack()

target_color_entry = tk.Entry(window, width=10)
target_color_entry.pack()

new_color_label = tk.Label(window, text="New Color (hex format):")
new_color_label.pack()

new_color_entry = tk.Entry(window, width=10)
new_color_entry.pack()

recolor_button = tk.Button(window, text="Recolor Image", command=recolor_button_clicked)
recolor_button.pack()

# Start the main event loop
window.mainloop()
