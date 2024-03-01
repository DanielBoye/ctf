import numpy as np
import matplotlib.pyplot as plt
import cv2
import os

script_path = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_path, 'ekorn.png')

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

print(img)
# Utfør Fourier-transformasjon
ft = np.fft.fft2(img)
fshift = np.fft.fftshift(ft)
spectrum = np.log(np.abs(fshift) + 1)  # Legg til 1 for å unngå log(0)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Originalt Bilde'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(spectrum, cmap='gray')
plt.title('Fourier Spektrum'), plt.xticks([]), plt.yticks([])

plt.show()
