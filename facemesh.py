import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    
    frame_h, frame_w, _ = frame.shape
    landmark_points = output.multi_face_landmarks

    if landmark_points:

        for face_landmarks in landmark_points:
            for idx, landmark in enumerate(face_landmarks.landmark):

                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)

                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow('Face Mesh', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
