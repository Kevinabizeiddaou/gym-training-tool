import cv2
import joblib
import numpy as np
import PoseModule as pm

def extract_features_from_lmList(lmList):
    if len(lmList) == 0:
        return None
    landmarks = np.array(lmList)[:,1:]
    mean = np.mean(landmarks, axis=0)
    std = np.std(landmarks, axis=0) + 1e-6
    normalized = (landmarks - mean) / std
    return normalized.flatten()

def main():
    # Load models
    form_model = joblib.load('form_model.pkl')   # Good vs Bad
    state_model = joblib.load('state_model.pkl') # Up vs Down

    cap = cv2.VideoCapture(0)
    detector = pm.poseDetector()

    count = 0
    direction = None  # track "Up" or "Down"
    feedback = "Fix Form"

    while True:
        ret, img = cap.read()
        if not ret:
            break

        img = detector.findPose(img, False)
        lmList = detector.findPosition(img, False)
        features = extract_features_from_lmList(lmList)

        form_prediction = "Fix Form"
        state_prediction = None

        if features is not None:
            # Predict form
            form_prediction = form_model.predict([features])[0]  # "Good" or "Bad"
            # Predict state
            state_prediction = state_model.predict([features])[0]  # "Up" or "Down"

        # If form is good, we trust the state for counting
        # If form is bad, we don't increment count, just show "Fix Form"
        if form_prediction == "Good" and state_prediction is not None:
            feedback = state_prediction
            # Counting logic based on transitions
            if direction is None:
                direction = state_prediction
            else:
                if direction == "Up" and state_prediction == "Down":
                    count += 0.5
                    direction = "Down"
                elif direction == "Down" and state_prediction == "Up":
                    count += 0.5
                    direction = "Up"
        else:
            feedback = "Fix Form"

        # Draw UI
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 5)

        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)

        # Display form quality too
        cv2.putText(img, f"Form: {form_prediction}", (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)

        cv2.imshow('Pushup Counter - ML Based', img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
