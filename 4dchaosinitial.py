from PIL import Image

def normalize(value, max_value):
    # Normalize the value to the valid range (0 to max_value-1)
    return value % max_value

def apply_4d_chaotic_equations(input_image_path, output_image_path, a1, a2, a3, a4, a5, a6, initial_x, initial_y, initial_z, initial_w):
    # Load the input image
    input_image = Image.open(input_image_path).convert('L')
    width, height = input_image.size

    # Create a blank output image
    output_image = Image.new('L', (width, height))

    # Initialize the system variables
    x = initial_x
    y = initial_y
    z = initial_z
    w = initial_w

    # Iterate over each pixel in the image
    for x_pixel in range(width):
        for y_pixel in range(height):
            # Get the pixel value
            pixel_value = input_image.getpixel((x_pixel, y_pixel))

            # Apply the 4D chaotic equations
            x_new = normalize(a1 * x + y * z + a2 * w ** 2 + a3, 256)
            y_new = normalize(a4 * y - x * z + abs(w) * y, 256)
            z_new = normalize(x * y + a5 * z, 256)
            w_new = normalize(w + a6 * z, 256)

            # Update the system variables
            x = x_new
            y = y_new
            z = z_new
            w = w_new

            # XOR the pixel value with the transformed value
            transformed_pixel_value = pixel_value ^ int(x_new) ^ int(y_new) ^ int(z_new) ^ int(w_new)

            # Set the result as the pixel value in the output image
            output_image.putpixel((x_pixel, y_pixel), transformed_pixel_value)

    # Save the output image
    output_image.save(output_image_path)

# Example usage for XOR with four different images and equations
input_image_1 = 'output_xor1.png'
input_image_2 = 'output_xor2.png'
input_image_3 = 'output_xor3.png'
input_image_4 = 'output_xor4.png'
output_image_1 = 'output1.png'
output_image_2 = 'output2.png'
output_image_3 = 'output3.png'
output_image_4 = 'output4.png'
a1 = 12
a2 = 0.05
a3 = 0.4
a4 = 8
a5 = 45
a6 = 10
initial_x = 0.02
initial_y = 0.01
initial_z = 0.03
initial_w = 0.04

apply_4d_chaotic_equations(input_image_1, output_image_1, a1, a2, a3, a4, a5, a6, initial_x, initial_y, initial_z, initial_w)
apply_4d_chaotic_equations(input_image_2, output_image_2, a1, a2, a3, a4, a5, a6, initial_x, initial_y, initial_z, initial_w)
apply_4d_chaotic_equations(input_image_3, output_image_3, a1, a2, a3, a4, a5, a6, initial_x, initial_y, initial_z, initial_w)
apply_4d_chaotic_equations(input_image_4, output_image_4, a1, a2, a3, a4, a5, a6, initial_x, initial_y, initial_z, initial_w)