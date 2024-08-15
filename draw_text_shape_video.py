import cv2
import datetime

video = cv2.VideoCapture("video.mp4")
# For Webcam
# video = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_COMPLEX
text = 'Height: ' + str(video.get(4)) + ' Width: ' + str(video.get(3))
print("Width ", video.get(3))  # 3 means width
print("Height ", video.get(4))  # 4 means height
print("Time ", datetime.datetime.now())

while video.isOpened():
    ret, frame = video.read()
    if ret:
        date_text = "Date: " + str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (0, 40), font, 0.5, (0, 125, 255),
                            1, cv2.LINE_AA)
        frame = cv2.putText(frame, date_text, (0, 60), font, 0.5, (0, 125, 255),
                            1, cv2.LINE_AA)
        frame = cv2.rectangle(frame, (200, 10), (400, 128), (128, 0, 255), 8)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()
