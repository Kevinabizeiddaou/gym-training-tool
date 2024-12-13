# AI Gym Trainer

An AI-powered gym trainer that monitors users' exercise form, counts repetitions, and provides real-time feedback to improve workout quality and safety.

## Features
- **Pose Detection and Analysis**: Tracks joint movements during exercises and identifies posture issues (e.g., knees misaligned during squats).
- **Repetition Counting**: Accurately counts exercise repetitions in real time.
- **Form Evaluation**: Scores each repetition based on posture correctness (scale: 0-1).
- **Workout Tracking**: Logs weights, tracks progress over time, and displays visual graphs of user improvements.
- **Interactive Feedback**: Alerts users about common mistakes in form (e.g., arching back during push-ups).

## Technologies Used
- **Programming Languages**: Python
- **Pose Estimation**: Mediapipe
- **Machine Learning Models**: CNNs and Random Forest Classifiers for form evaluation and repetition counting
- **Data**: COCO, and custom exercise datasets
- **Backend**: Flask/Django for server-side processing

## How to Run
### Prerequisites
- Python 3.8+
- Git


### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Kevinabizeiddaou/gym-training-tool.git
   cd gym-training-tool
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the models to train them, then test.
  


## Project Workflow
1. **Pose Detection**: Mediapipe extracts pose landmarks from webcam/video.
2. **Repetition Counting**: Detects complete exercise cycles.
3. **Form Evaluation**: Scores repetitions using a trained CNN model.
4. **Feedback Loop**: Provides real-time alerts for posture corrections.

## Folder Structure
```bash
ai-gym-trainer/
├── backend/                  # Backend server files
│   ├── models                # Main python files
│   ├── routes/               # API endpoints
│   ├── models/               # Machine learning models
│   ├── utils/                # Utility scripts
├── data/                     # Datasets for training and testing
│   ├── raw/                  # Raw datasets
│   ├── processed/            # Processed datasets
├── models/                   # Pre-trained and custom models
│   ├── form_evaluation/      # CNN models
│   ├── repetition_counting/  # Random Forest Classifiers
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
```

## Future Enhancements
- Multi-language support.
- Support for additional exercise types.
- Integration with smart fitness devices.
- Gamification features (badges, leaderboards, etc.).

## Acknowledgments
- **Mediapipe** for pose detection.
- **COCO Dataset** for training data.
- **Onyx Fitness** for inspiration.


