import cv2
import pyautogui as pag
import numpy as np

# Capture screen resolution
rs = pag.size()

# Set the frame rate
fps = 10
# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('ss.avi', fourcc, fps, rs)  # Output file, codec, FPS, resolution

# Create recording module
cv2.namedWindow("Live Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Recording", (640, 480))

while True:
    ss = pag.screenshot()
    img = np.array(ss)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out.write(img_rgb)
    cv2.imshow("Live Recording", img_rgb)
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()



