import sys
from skimage.measure import compare_ssim as ssim 
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
import os

directory = sys.argv[1]

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

def compare_images(imageA, imageB):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB, multichannel=True)
	
	return m, s


def compare_and_show_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m, s = compare_images(imageA, imageB)

	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))

	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")

	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")

	# show the images
	plt.show()

# load the images -- the original, the original + contrast,
# and the original + photoshop
image_file_names = [x for x in os.listdir(str(directory)) if x[-4:] == ".png"]
images = []

print image_file_names
for file_name in image_file_names:
	image_title = file_name.split(".png")[0]
	raw_image = cv2.imread(str(directory) + file_name)
	bnw_image = raw_image.sum(-1)
	images += [(image_title, raw_image)]

	# original = cv2.imread(str(directory) + file_name)
	# contrast = cv2.imread(str(directory) + "new.png")
	# shopped = cv2.imread("images/jp_gates_photoshopped.png")

# convert the images to grayscale
#original_grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#contrast_grayscale = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
#shopped_grayscale = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
#images = ("Original", original), ("Contrast", contrast), ("Original Gray", original_grayscale), ("Contrast Gray", contrast_grayscale)#, ("Photoshopped", shopped)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(len(images), 1, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()

# compare the images
#compare_images(original, original, "Baseline vs Baseline")
#compare_images(original, contrast, "Baseline vs. Contrast")
#compare_images(original, original_grayscale, "Baseline vs. Baseline GrayScale")
#compare_images(contrast, contrast_grayscale, "Contrast vs. Contrast GrayScale")
#compare_images(original, contrast_grayscale, "Baseline vs. Contrast GrayScale")
#compare_images(original_grayscale, contrast_grayscale, "Baseline GrayScale vs. Contrast GrayScale")
#compare_images(original, contrast, "Original vs. Contrast")
#compare_images(original, shopped, "Original vs. Photoshopped")

#shot_one = 

#This file is meant to do image comparison
#