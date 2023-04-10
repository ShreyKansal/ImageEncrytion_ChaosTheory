from PIL import Image

key_img = Image.open('C:/Users/skans/OneDrive/Desktop/chaos/standard_test_images-20230410T195153Z-001/standard_test_images/fruits.png')
img1 = Image.open('red.png')
img2 = Image.open('green.png')
img3 = Image.open('blue.png')
img4 = Image.open('green.png')

output1 = Image.new('RGB', key_img.size)
output2 = Image.new('RGB', key_img.size)
output3 = Image.new('RGB', key_img.size)
output4 = Image.new('RGB', key_img.size)

for x in range(key_img.width):
    for y in range(key_img.height):
        key_pixel = key_img.getpixel((x, y))
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        pixel3 = img3.getpixel((x, y))
        pixel4 = img4.getpixel((x, y))
        
        # ye maine net pe dekha wo actually grayscale image ka mode change krke rgb rkhna padta h toh uska sasta jugaad h
        if img1.mode == "L":
            pixel1 = (pixel1, pixel1, pixel1)
        if img2.mode == "L":
            pixel2 = (pixel2, pixel2, pixel2)
        if img3.mode == "L":
            pixel3 = (pixel3, pixel3, pixel3)
        if img4.mode == "L":
            pixel4 = (pixel4, pixel4, pixel4)
        
        # xor yaha pe shuru h 
        red1, green1, blue1 = key_pixel
        red2, green2, blue2 = pixel1
        red3, green3, blue3 = pixel2
        red4, green4, blue4 = pixel3
        red5, green5, blue5 = pixel4
        
        red_result1 = red1 ^ red2
        green_result1 = green1 ^ green2
        blue_result1 = blue1 ^ blue2
        
        red_result2 = red1 ^ red3
        green_result2 = green1 ^ green3
        blue_result2 = blue1 ^ blue3
        
        red_result3 = red1 ^ red4
        green_result3 = green1 ^ green4
        blue_result3 = blue1 ^ blue4
        
        red_result4 = red1 ^ red5
        green_result4 = green1 ^ green5
        blue_result4 = blue1 ^ blue5
        
        output1.putpixel((x, y), (red_result1, green_result1, blue_result1))
        output2.putpixel((x, y), (red_result2, green_result2, blue_result2))
        output3.putpixel((x, y), (red_result3, green_result3, blue_result3))
        output4.putpixel((x, y), (red_result4, green_result4, blue_result4))

output1.save('output_xor1.png')
output2.save('output_xor2.png')
output3.save('output_xor3.png')
output4.save('output_xor4.png')
