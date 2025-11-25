🐾 Wild Animal Detection and Alerting System

The Wild Animal Detection and Alerting System is an AI-based solution that detects the presence of wild animals in real time using deep learning and triggers automated alerts. This system can help prevent human–animal conflict, protect farms, and improve safety in forest-border regions.

🚀 Features

✔ Real-time video detection using YOLOv5

✔ High-accuracy object recognition for animals such as tigers, elephants, deer, etc.

✔ Alert generation (email/SMS/push notification depending on setup)

✔ Firebase integration for live data storage

✔ Lightweight & easy to deploy

✔ Works with webcam, external camera, or video files

🧠 Tech Stack

Python

YOLOv5

OpenCV

Firebase Admin SDK

Numpy

PIL / Torch

📁 Project Structure
Wild-Animal-Detection-and-Alerting-System/
│
├── yolov5/                 # YOLOv5 model & utils
├── models/                 # Custom trained YOLO weights
├── scripts/                # Supporting Python scripts
├── main.py                 # Main detection script
├── requirements.txt        # Required dependencies
├── README.md               # Documentation
└── ...

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/Sham172004/Wild-Animal-Detection-and-Alerting-System.git
cd Wild-Animal-Detection-and-Alerting-System

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Download or add your YOLOv5 model

Place your trained model (example: best.pt) inside:

models/

4️⃣ Add Firebase credentials

Create a file:

firebase_credentials.json


⚠ DO NOT upload this file to GitHub.
Add it to .gitignore.

Your Firebase service account file looks like this:

{
  "type": "service_account",
  "project_id": "...",
  "private_key": "...",
  ...
}

▶️ Running the System
Run detection using webcam:
python main.py --source 0

Run detection on a video file:
python main.py --source path/to/video.mp4

Run in image mode:
python main.py --source image.jpg

📡 Alert System

Whenever an animal is detected:

The detection result is uploaded to Firebase

Alerts can be triggered using:

SMS (Twilio)

Email (SMTP)

Push notifications

Custom mobile app / dashboard

This can be configured inside:

alert_system.py

📊 Output Example

Bounding boxes around detected animals

Label + Confidence score

Timestamp sent to Firebase

Alert triggered when confidence > threshold

🔒 Security Notes

Never upload API keys or Firebase credentials to GitHub

Use environment variables to store secrets

Your .json service key must always be inside .gitignore

🤝 Contribution

Pull requests are welcome.
Feel free to open issues if you want new features or find bugs.

📜 License

This project is for educational & research use.
You may extend or modify it for real-world applications.
