import cv2
import streamlit as st

st.title("Smile Detector Application")
st.write('Press Q to close the window')
run = st.checkbox('Run Smile Detector')


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while run:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    font = cv2.FONT_HERSHEY_PLAIN

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 15)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+w, x:x+w]
        smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 9)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)
            if len(smile) > 0:
                cv2.putText(frame, 'Smiling', (200, height - 10), font, 4 ,(0, 0, 0), 5, cv2.LINE_AA)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
else:
    st.write('Stopped')

cap.release()
cv2.destroyAllWindows()
