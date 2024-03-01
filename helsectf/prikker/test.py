from PIL import Image
import os

# Coordinates of the dot in your images
x_coordinate = 100  # Adjust as needed
y_coordinate = 100  # Adjust as needed

# Function to extract dot from each image
def extract_dot(image_path):
    try:
        img = Image.open(image_path)
        dot = img.getpixel((x_coordinate, y_coordinate))
        return dot
    except OSError as e:
        print(f"Error processing {image_path}: {e}")
        return None  # Return None for failed images

# Function to create a blank canvas
def create_blank_canvas(width, height):
    return Image.new('RGB', (width, height), (255, 255, 255))  # White background

# Directory containing your GIF images
gif_directory = "C:\\Users\\danie\\Downloads\\ezgif-1-07f303cbf0-gif-im"

# Output image path
output_image_path = "output.png"

# Set the size of the output canvas
canvas_width = 8000  # Adjust as needed
canvas_height = 6000  # Adjust as needed

# Create a blank canvas
canvas = create_blank_canvas(canvas_width, canvas_height)

# Loop through each GIF image in the directory
for filename in os.listdir(gif_directory):
    if filename.endswith(".gif"):
        gif_path = os.path.join(gif_directory, filename)
        dot_color = extract_dot(gif_path)

        if dot_color is not None:
            # Create an image with the dot color
            dot_image = Image.new('RGB', (1, 1), dot_color)

            # Paste the dot onto the canvas
            canvas.paste(dot_image, (x_coordinate, y_coordinate))

# Save the combined image
canvas.save(output_image_path)
