from PIL import Image

def extract_message_from_png(file_path):
    try:
        image = Image.open(file_path)

        # Check the size of the image
        width, height = image.size
        if height != 16:
            raise ValueError("The image height is not 16 pixels.")

        # Convert the image to grayscale (assuming it's black and white)
        grayscale_image = image.convert("L")

        # Generate the path for the grayscale image
        grayscale_file_path = file_path.replace(".png", "_grayscale.png")

        # Save the grayscale image
        grayscale_image.save(grayscale_file_path)

        # Extract the bytes and convert to ASCII characters
        message = ""
        for y in range(height):
            char_code = 0
            for x in range(width):
                pixel_value = grayscale_image.getpixel((x, y))
                char_code = (char_code << 1) | (pixel_value < 128)

            # Convert char_code to ASCII character
            message += chr(char_code)

        # Check if the message contains only ASCII characters
        is_ascii = all(ord(c) < 128 for c in message)

        return message, grayscale_file_path, is_ascii
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None

if __name__ == "__main__":
    file_path = "secret.png"
    message, grayscale_file_path, is_ascii = extract_message_from_png(file_path)
    if message:
        print("Hidden Message:")
        print(message)
        print("Grayscale image saved as:", grayscale_file_path)
        if is_ascii:
            print("Encoding: ASCII")
        else:
            print("Encoding: UTF-8")
