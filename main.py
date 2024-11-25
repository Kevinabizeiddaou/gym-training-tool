import cv2
from pose_detection import PoseDetector
from pushup_detection import PushupCounter

def main():
    # Initialize components
    pose_detector = PoseDetector()
    pushup_counter = PushupCounter()

    # Start webcam
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Unable to read from webcam. Exiting...")
            break

        # Detect pose landmarks
        results = pose_detector.detect_pose(frame)
        landmarks = results.pose_landmarks.landmark if results.pose_landmarks else None

        # Process push-up detection
        counter, stage = pushup_counter.process_pushup(landmarks)

        # Draw landmarks
        frame = pose_detector.draw_landmarks(frame, results)

        # Display push-up count and stage
        cv2.putText(frame, f"Push-up Count: {counter}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f"Stage: {stage}", (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # Show the frame
        cv2.imshow("AI Gym Trainer", frame)

        # Break on 'q' key press
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    pose_detector.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
