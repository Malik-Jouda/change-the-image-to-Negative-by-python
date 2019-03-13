#hwo change the image to Negative by python => Pillow
# install: pip install Pillow
# import Image
# import PIL.ImageOps

from PIL import Image
import PIL.ImageOps
image = input("Enter The Image : ")

# Open The Image
image = Image.open(image)

# change the image to Negative
inverted_image = PIL.ImageOps.invert(image)

# Save Image
inverted_image.save("result.jpg")

# show Image
inverted_image.show()