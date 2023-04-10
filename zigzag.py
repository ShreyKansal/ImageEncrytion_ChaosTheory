import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('C:/Users/skans/OneDrive/Pictures/testimage.png')

width, height = img.size

blocks = np.array(img).reshape(height // 8, 8, -1, 8, 4).swapaxes(1, 2).reshape(-1, 8, 8, 4)

zigzag_order = np.array([
    0, 1, 8, 16, 9, 2, 3, 10,
    17, 24, 32, 25, 18, 11, 4, 5,
    12, 19, 26, 33, 40, 48, 41, 34,
    27, 20, 13, 6, 7, 14, 21, 28,
    35, 42, 49, 56, 57, 50, 43, 36,
    29, 22, 15, 23, 30, 37, 44, 51,
    58, 59, 52, 45, 38, 31, 39, 46,
    53, 60, 61, 54, 47, 55, 62, 63
])

blocks_flat = []
for block in blocks:
    block_flat = block.reshape(-1, 4)[zigzag_order].flatten()
    blocks_flat.append(block_flat)

# Print the flattened blocks
# for i, block_flat in enumerate(blocks_flat):
# print(f'Block {i}:\n{block_flat}\n') 

img_reconstructed = np.array(blocks_flat).reshape(height // 8, -1, 8, 4).swapaxes(1, 2).reshape(height, width, 4)
plt.imshow(img_reconstructed.astype('uint8'))
plt.show()

