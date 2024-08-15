import cv2

video = cv2.VideoCapture("video.mp4")
ret, image = video.read()
count = 0

while True:
    if ret:
        cv2.imwrite(f"frames/img{count}.jpg", image)
        video.set(cv2.CAP_PROP_POS_MSEC, (count*30))
        ret, image = video.read()
        cv2.imshow("Frame", image)
        count += 1
        if cv2.waitKey(1) == ord("q"):
            break


video.release()
cv2.destroyAllWindows()