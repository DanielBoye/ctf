import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

script_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_path, 'blabr.png')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

ft = np.fft.fft2(img)
fshift = np.fft.fftshift(ft)

rows, cols = img.shape
crow, ccol = rows // 2 , cols // 2
mask = np.ones((rows, cols), np.uint8)
r = 30  
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 0

fshift_hp = fshift * mask

img_hp = np.fft.ifft2(np.fft.ifftshift(fshift_hp)).real

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Originalt Bilde'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(np.log(np.abs(fshift) + 1), cmap='gray')
plt.title('Fourier Spektrum'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(img_hp, cmap='gray')
plt.title('Bilde etter High-pass Filter'), plt.xticks([]), plt.yticks([])

plt.show()
