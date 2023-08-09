from PIL import Image
from collections import Counter


def get_main_colour():
    # ChatGPT Code:

    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGB mode (if not already)
    image = image.convert("RGB")

    # Get the image's pixel data
    pixels = list(image.getdata())

    # Count the occurrence of each pixel color
    color_counter = Counter(pixels)

    # Find the most common color (prevalent color)
    most_common_color = color_counter.most_common(1)[0][0]

    return most_common_color

# Replace 'your_image_path.jpg' with the actual path to your image file
image_path = 'your_image_path.jpg'
prevalent_color = get_most_prevalent_color(image_path)
print("Most Prevalent Color:", prevalent_color)

def main():
    pass
