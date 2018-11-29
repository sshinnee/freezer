import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
from PIL import Image
from skimage import measure

directory = sys.argv[1]

# Construct some test data
x, y = np.ogrid[-np.pi:np.pi:100j, -np.pi:np.pi:100j]
#r = np.sin(np.exp((np.sin(x)**3 + np.cos(y)**2)))
#cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
img_raw = cv2.imread(str(directory) + "baseline.png")
#img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
img = img_raw.sum(-1) 
#img = np.sqrt((img_raw*img_raw).sum(-1)) #takes -significantly longer to process- too long to process, did not convert it
#img_raw_pil = Image.open(str(directory) + "baseline.png")
#img = np.asarray(img_raw_pil.convert('L'))
# if img:
# 	print "image is not None"

# Find contours at a constant value of 0.8
contours = measure.find_contours(img, 0.8)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(img, interpolation='nearest', cmap=plt.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])
plt.show()