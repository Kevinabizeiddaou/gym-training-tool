AI Gym Trainer
An AI-powered gym trainer that monitors users' exercise form, counts repetitions, and provides real-time feedback to improve workout quality and safety.

Features
Pose Detection and Analysis:
Tracks joint movements during exercises.
Identifies posture issues (e.g., knees misaligned during squats).
Repetition Counting:
Accurately counts exercise repetitions in real-time.
Form Evaluation:
Scores each repetition based on posture correctness (scale: 0-1).
Workout Tracking:
Logs weights and tracks progress over time.
Provides visual graphs of user improvements.
Interactive Feedback:
Alerts users about common mistakes in form (e.g., arching back during push-ups).
Technologies Used
Programming Languages: Python, JavaScript
Pose Estimation: Mediapipe
Machine Learning Models: CNNs and RNNs for form evaluation and repetition counting
Data: COCO, MPII, and custom exercise datasets
Frontend: ReactJS (optional for UI development)
Backend: Flask/Django for server-side processing
How to Run
Prerequisites
Python 3.8+
Git
Node.js (if working with ReactJS frontend)
Setup
Clone the repository:
bash
Copy code
git clone https://github.com/<your-username>/ai-gym-trainer.git
cd ai-gym-trainer
Install required Python packages:
bash
Copy code
pip install -r requirements.txt
Run the backend server:
bash
Copy code
python app.py
(Optional) Start the frontend ReactJS app:
bash
Copy code
cd frontend
npm install
npm start
Project Workflow
Pose Detection: Mediapipe extracts pose landmarks from webcam/video.
Repetition Counting: Detects complete exercise cycles.
Form Evaluation: Scores repetitions using a trained CNN model.
Feedback Loop: Provides real-time alerts for posture corrections.
Folder Structure
bash
Copy code
ai-gym-trainer/
│
├── backend/                  # Backend server files
├── data/                     # Datasets for training and testing
├── frontend/                 # Frontend ReactJS application
├── models/                   # Pre-trained and custom models
├── utils/                    # Helper scripts (e.g., data processing)
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
Contributing
Contributions are welcome! Here's how you can help:

Fork the repository.
Create a branch (git checkout -b feature-name).
Commit your changes (git commit -m "Added new feature").
Push the branch (git push origin feature-name).
Open a pull request.
Future Enhancements
Multi-language support.
Support for additional exercise types.
Integration with smart fitness devices.
Acknowledgments
Mediapipe
COCO Dataset
Onyx Fitness
License
This project is licensed under the MIT License. See the LICENSE file for more details.
