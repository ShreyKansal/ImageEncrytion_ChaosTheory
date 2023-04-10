from PIL import Image
image = Image.open('C:/Users/skans/OneDrive/Pictures/testimage.png')
red, green, blue = image.split()
red.save("red.jpg")
green.save("green.jpg")
blue.save("blue.jpg")

