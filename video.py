import cv2

# Read and play video from a file
# cap = cv2.VideoCapture("video.mp4")
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame", frame)
#     cv2.imshow("Gray", gray)
#     k = cv2.waitKey(25)
#     if k == ord("q"):
#         break

# Capture video from webcam save to memory
cap = cv2.VideoCapture(0)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Define codec (e.g., XVID, MJPG, etc.)
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))  # Output file, codec, FPS, resolution

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out.write(frame)
        cv2.imshow("Webcam", frame)
        # cv2.imshow("Gray", gray)
        if cv2.waitKey(1) == ord("q"):
            break

# Release video capture object and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()
