from PIL import Image

# Open your image
image = Image.open("logo.png")  # Ensure the image is in the same directory

# Flip the image horizontally (left to right)
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

# Save and show the flipped image
flipped_image.save("logo_flipped.png")
flipped_image.show()