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
    image.save("recolored_345435image.png")

# Prompt for input
image_path = input("Enter the local image path: ")
target_color_hex = input("Enter the target color (hex format, e.g., #RRGGBB): ")
new_color_hex = input("Enter the new color (hex format, e.g., #RRGGBB): ")

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
