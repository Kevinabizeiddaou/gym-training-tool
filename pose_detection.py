import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, detection_confidence=0.5, tracking_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.pose = self.mp_pose.Pose(min_detection_confidence=detection_confidence,
                                      min_tracking_confidence=tracking_confidence)

    def detect_pose(self, frame):
        """Detect pose landmarks in the given frame."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb_frame)
        return results

    def draw_landmarks(self, frame, results):
        """Draw pose landmarks on the given frame."""
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame, 
                results.pose_landmarks, 
                self.mp_pose.POSE_CONNECTIONS
            )
        return frame

    def close(self):
        """Release pose detector resources."""
        self.pose.close()
