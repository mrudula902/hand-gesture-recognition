import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Gesture mapping function
def get_gesture(landmarks):
    # Simplified logic based on finger positions
    thumb = landmarks[4].x < landmarks[3].x       # thumb up
    index = landmarks[8].y < landmarks[6].y       # index finger up
    middle = landmarks[12].y < landmarks[10].y    # middle finger up
    ring = landmarks[16].y < landmarks[14].y      # ring finger up
    pinky = landmarks[20].y < landmarks[18].y     # pinky finger up

    # Open palm
    if all([thumb, index, middle, ring, pinky]):
        return "Stop"
    # Fist
    elif not any([thumb, index, middle, ring, pinky]):
        return "No"
    # Thumbs up (only thumb)
    elif thumb and not any([index, middle, ring, pinky]):
        return "Yes"
    # Peace (index + middle)
    elif index and middle and not any([ring, pinky, thumb]):
        return "Peace"
    # Index finger up
    elif index and not any([middle, ring, pinky, thumb]):
        return "Hello"
    else:
        return "Unknown"

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesture = get_gesture(hand_landmarks.landmark)
            cv2.putText(frame, f"Gesture: {gesture}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture to Text", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
