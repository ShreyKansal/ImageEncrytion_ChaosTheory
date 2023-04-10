import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# load image
img = Image.open('C:/Users/skans/OneDrive/Pictures/testimage.png')

# split image into 8x8 blocks
w, h = img.size
blocks = []
for i in range(0, h, 8):
    for j in range(0, w, 8):
        block = np.asarray(img.crop((j, i, j+8, i+8)))
        blocks.append(block)

# perform zig zag transformation on each block
zigzag_blocks = []
for block in blocks:
    zigzag_block = np.zeros_like(block)
    for k in range(0, 8):
        for i in range(0, k+1):
            j = k - i
            if k % 2 == 0:
                zigzag_block[i, j] = block[j, i]
            else:
                zigzag_block[j, i] = block[i, j]
    for k in range(7, 0, -1):
        for i in range(0, k):
            j = k - i
            if k % 2 == 0:
                zigzag_block[8-i-1, 8-j-1] = block[8-j-1, 8-i-1]
            else:
                zigzag_block[8-j-1, 8-i-1] = block[8-i-1, 8-j-1]
    zigzag_blocks.append(zigzag_block)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

img_transformed = np.zeros_like(np.asarray(img))
for i in range(0, h, 8):
    for j in range(0, w, 8):
        idx = i//8 * (w//8) + j//8
        img_transformed[i:i+8, j:j+8] = zigzag_blocks[idx]
        
plt.subplot(1, 2, 2)
plt.imshow(img_transformed)
plt.title('Transformed Image')
plt.axis('off')

plt.show()
