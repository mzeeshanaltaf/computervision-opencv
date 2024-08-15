import cv2

# Reading, resizing and displaying of an image
img = cv2.imread("Team.jpeg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (512, 512))
cv2.imshow("Original Image", img)

# Image flipping
# 0 - Flips the image vertically
# 1 - Flips the image horizontally
# -1 - Flips the image both horizontally and vertically
img_flip = cv2.flip(img, -1)
cv2.imshow("Re-sized Image", img_flip)

# Convert image to grayscale
# img_gs = cv2.imread("Team.jpeg", cv2.IMREAD_GRAYSCALE)
# img_gs = cv2.resize(img_gs, (512, 512))
# cv2.imshow("Gray Scale Image", img_gs)

cv2.waitKey()
cv2.destroyAllWindows()
