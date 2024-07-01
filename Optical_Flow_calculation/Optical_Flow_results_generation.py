import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Define which frame you want (3 digits)
i = '...'

# Acquire Depth images 

depth_1_img = np.load('...depth/000{num}_depth.npy'.format(num = i))
depth_2_img = np.load('.../depth/000{num}_depth.npy'.format(num = i))

# Load Optical flows (DA, DROID, DA-DROID) for the frame
Opt_1_img = mpimg.imread('.../000{num}/bgr.jpg'.format(num = i))
Opt_2_img = mpimg.imread('.../000{num}/bgr.jpg'.format(num = i))
diff_opt = Opt_1_img - Opt_2_img

# Plot the results

plt.subplot(1, 5, 1)
plt.imshow(depth_1_img, cmap='Greys')
plt.axis('off')
plt.subplot(1, 5, 2)
plt.imshow(depth_2_img, cmap='Greys')
plt.axis('off')
plt.subplot(1, 5, 3)
plt.imshow(Opt_1_img)
plt.axis('off')
plt.subplot(1, 5, 4)
plt.imshow(Opt_2_img)
plt.axis('off')
plt.subplot(1, 5, 5)
plt.imshow(diff_opt)
plt.axis('off')
plt.subplots_adjust(wspace = 0, hspace = 0)

plt.show()
