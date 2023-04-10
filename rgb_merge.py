from PIL import Image

red_channel = Image.open("red_channel.jpg")
green_channel = Image.open("green_channel.jpg")
blue_channel = Image.open("blue_channel.jpg")
rgb_image = Image.merge("RGB", (red_channel, green_channel, blue_channel))
rgb_image.save("Merge krdi si.jpg")
