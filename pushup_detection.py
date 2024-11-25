
from utils import calculate_angle

class PushupCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None  # 'up' or 'down'

    def process_pushup(self, landmarks):
        """
        Process landmarks to determine push-up stage and count.
        :param landmarks: List of pose landmarks
        """
        if not landmarks:
            return self.counter, self.stage

        # Extract key points
        shoulder = [landmarks[11].x, landmarks[11].y]  # Left shoulder
        elbow = [landmarks[13].x, landmarks[13].y]     # Left elbow
        wrist = [landmarks[15].x, landmarks[15].y]     # Left wrist
        hip = [landmarks[23].x, landmarks[23].y]       # Left hip

        # Calculate angles
        elbow_angle = calculate_angle(shoulder, elbow, wrist)
        shoulder_angle = calculate_angle(hip, shoulder, elbow)

        # Push-up logic
        if elbow_angle > 160 and self.stage == 'down':
            self.stage = 'up'
            self.counter += 1

        if elbow_angle < 90 and shoulder_angle > 40:
            self.stage = 'down'

        return self.counter, self.stage
