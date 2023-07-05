from PIL import Image

def identify_color(image_path, x, y):
    # Open the image
    image = Image.open(image_path)

    # Get the pixel value at the specified coordinates
    pixel = image.getpixel((x, y))

    # Check if the pixel has an alpha channel
    if len(pixel) == 4:
        # Ignore the alpha channel value
        r, g, b, _ = pixel
    elif len(pixel) >= 3:
        r, g, b = pixel[:3]
    else:
        print("Invalid pixel format.")
        return

    # Print the RGB values
    print("RGB values at coordinates ({}, {}): ({}, {}, {})".format(x, y, r, g, b))

# Usage
image_path = r"C:\Users\jishn\c programs\freecodecampcpp\FORESTFIRE\worldgnbl.png"  # Replace with the path to your image
x = 256  # X-coordinate of the pixel
y = 256  # Y-coordinate of the pixel
identify_color(image_path, x, y)
