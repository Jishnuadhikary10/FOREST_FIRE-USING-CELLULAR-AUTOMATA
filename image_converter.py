from PIL import Image

def convert_image(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB color mode
    image = image.convert("RGB")

    # Create a new image for the converted pixels
    converted_image = Image.new("RGB", image.size)
    pixels = converted_image.load()
    width, height = converted_image.size

    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))

            # Convert shades of blue to (0, 0, 255)
            if b > r and b > g:
                pixels[x, y] = (0, 0, 255)

            # Convert shades of green to (0, 255, 0)
            if g > r and g > b:
                pixels[x, y] = (0, 255, 0)

    # Save the converted image
    output_path = r"C:\Users\jishn\c programs\freecodecampcpp\FORESTFIRE\converted_image.png"
    converted_image.save(output_path)
    print("Image converted and saved as", output_path)

# Usage
image_path = r"C:\Users\jishn\c programs\freecodecampcpp\FORESTFIRE\worldgnbl.png"
convert_image(image_path)
