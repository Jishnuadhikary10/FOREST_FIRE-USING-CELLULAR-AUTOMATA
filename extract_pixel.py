from PIL import Image

def extract_pixels(image_path):
    # Load the image
    image = Image.open(image_path)

    # Convert the image to RGB mode (if it's not already)
    image = image.convert("RGB")

    # Get the width and height of the image
    width, height = image.size

    # Create an empty 2D array to store the pixel values
    pixel_data = [[None] * width for _ in range(height)]

    # Iterate over each pixel and extract its RGB values
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))

            # Assign green to trees and blue to water
            if r == 0 and g == 255 and b == 0:
                pixel_data[y][x] = 'TREE'
            elif r == 0 and g == 0 and b == 255:
                pixel_data[y][x] = 'WATER'
            else:
                pixel_data[y][x] = 'EMPTY'

    return pixel_data

# Example usage
image_path = r"C:\Users\jishn\c programs\freecodecampcpp\FORESTFIRE\worldgnbl.png"  # Replace with the path to your image file
pixels = extract_pixels(image_path)

# Print the 2D array
for row in pixels:
    print(row)
