import cv2
import numpy as np

# img = cv2.imread("Team.jpeg")
# img = cv2.resize(img, (512, 512))

# Black image
# img = np.zeros([512, 512, 3], np.uint8) * 255

# White image
img = np.ones([512, 512, 3], np.uint8) * 255

# Draw a line/arrow/rectangle/circle on the image.
# Parameters (image, starting, ending, color, thickness). Color format is BGR
img = cv2.line(img, (0, 0), (200, 200), (245, 7, 31), 5)
img = cv2.arrowedLine(img, (0, 125), (255, 255), (255, 0, 125), 10)
img = cv2.rectangle(img, (384, 10), (510, 128), (128, 0, 255), 8)
img = cv2.circle(img, (225, 225), 50, (210, 255, 0), -5)

font = cv2.FONT_HERSHEY_COMPLEX
# Parameters (image, text, starting, font, font_size, color, thickness, line type)
img = cv2.putText(img, 'TEAM WORK', (0, 100), font, 2, (0, 125, 255), 2, cv2.LINE_AA)

# Function Signature: cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, thickness=1,
#                                   lineType=cv2.LINE_8, shift=0)
img = cv2.ellipse(img, (300,300), (100,50), 0, 0, 180, (0, 255, 0), 5)

cv2.imshow("Image", img)

# Quit if any key is pressed and then destroy all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
