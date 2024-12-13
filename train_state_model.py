import os
import cv2
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import PoseModule as pm

STATE_DIRS = {
    'Up': 'C:/Users/abize/Desktop/EECE/Year 3/Fall 24-25/EECE 490/UpPushUpDataset',
    'Down': 'C:/Users/abize/Desktop/EECE/Year 3/Fall 24-25/EECE 490/DownPushUpDataset'
}

def extract_features(img, detector):
    img = detector.findPose(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) == 0:
        return None
    landmarks = np.array(lmList)[:,1:]
    mean = np.mean(landmarks, axis=0)
    std = np.std(landmarks, axis=0) + 1e-6
    normalized = (landmarks - mean) / std
    return normalized.flatten()

def load_data(data_dirs):
    X, y = [], []
    detector = pm.poseDetector()
    for label, directory in data_dirs.items():
        if not os.path.exists(directory):
            continue
        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(directory, file)
                img = cv2.imread(img_path)
                if img is None:
                    continue
                f = extract_features(img, detector)
                if f is not None:
                    X.append(f)
                    y.append(label)
    return np.array(X), np.array(y)

if __name__ == "__main__":
    X, y = load_data(STATE_DIRS)
    if len(X) == 0:
        print("No state data found.")
        exit()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print("State Model Accuracy:", accuracy_score(y_test, preds))
    print("Classification Report:\n", classification_report(y_test, preds))

    joblib.dump(model, 'state_model.pkl')
    print("State model saved as state_model.pkl")
