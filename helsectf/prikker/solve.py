import os
import imageio
from PIL import Image

# Replace with the desired dimensions for your canvas
width = 3000
height = 2000

# Create a new blank image
result_image = Image.new('RGB', (width, height), (255, 255, 255))

# Specify the directory containing your images
image_folder = 'C:\\Users\\danie\\Downloads\\ezgif-1-07f303cbf0-gif-im'

# Initialize variables for positioning
x_position = 0
y_position = 0

# Loop through each image in the directory
for filename in os.listdir(image_folder):
    img_path = os.path.join(image_folder, filename)
    
    try:
        # Open the GIF using imageio
        gif = imageio.get_reader(img_path)
        
        # Iterate over each frame in the GIF
        for frame in gif:
            img = Image.fromarray(frame)

            # Paste each frame onto the blank canvas
            result_image.paste(img, (x_position, y_position))

            # Update the x and y positions for the next image
            x_position += img.width
            y_position += img.height

    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        continue  # Skip to the next iteration if there's an error

# Replace the file path with the desired path and filename for the combined image
result_image.save('aaa.png')  # Save as PNG to preserve transparency
