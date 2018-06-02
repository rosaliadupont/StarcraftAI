import numpy as np
import matplotlib.pyplot as plt

#create axes
ax1 = plt.subplot(111)

#create image plot
im1 = ax1.imshow(np.random.randint(0, high=256, size=(32,32)))

plt.ion()

while True:
    im1.set_data(np.random.randint(0, high=256, size=(32,32)))
    plt.pause(0.05)

plt.ioff() # due to infinite loop, this gets never called.
plt.show()