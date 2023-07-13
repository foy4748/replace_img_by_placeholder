import math
from PIL import Image, ImageDraw, ImageFont

def create_placeholder_image(width, height):
    # Create a new image with the specified resolution
    image = Image.new("RGB", (width, height), "lightgray")

    # Draw the resolution text on the image
    draw = ImageDraw.Draw(image)
    text = f"{width} x {height}"
    font_size = math.floor((width * 0.15))
    font = ImageFont.truetype("arial.ttf", font_size)  # Adjust the font and size as needed
    #text_width, text_height = draw.textsize(text, font=font)
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(text_position, text, fill="black", font=font)

    return image


# Define the desired image resolution
# width = 800
# height = 600

# Create the placeholder image
# placeholder_image = create_placeholder_image(width, height)

# Save the image to a file
# placeholder_image.save("placeholder_image.png")
