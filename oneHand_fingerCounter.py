import cv2
import handTracker



cap = cv2.VideoCapture(0)
detector = handTracker.HandTracker(maxHands=2)


while True:

    success, img = cap.read()
    img = detector.findHands(img)
    landmarks, _ = detector.findPosition(img)

    counter = []
    if len(landmarks) != 0:
        fingers = detector.fingersUp()
        #print(fingers)
        for i in fingers:
            if i==1:
                counter.append(1)
        number = len(counter)
        cv2.putText(img, str(number), (550, 80), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 255), 5)




    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key==27:
        break




cap.release()
cv2.destroyAllWindows()
