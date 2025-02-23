# 🧠🚀 YOLOv12-Based Object Detection and Live Tracking 🎥✨

Welcome to my project on Object Detection and Tracking using the latest YOLOv12 model! 🦾 YOLO (You Only Look Once) is one of the most powerful object detection models, and I’ve integrated it with live video feed tracking for a seamless and dynamic experience.

![Image](https://github.com/user-attachments/assets/e9f29a8b-1a01-478f-844b-4f3fa8b8a3fd)


# 🔥 What's This Project About?
This project combines real-time object detection and tracking:

1. YOLOv12 detects objects in live frames.

2. Users can manually select an object to track using CSRT Tracker.

3. The system continues tracking the selected object and provides a live overlay, even as it moves.


# 🌟 Why YOLOv12?
YOLOv12 is the latest version of the YOLO series and was released just 4 days ago (🔥 cutting-edge technology!). It comes with improvements in:

• ⚡ Speed: Real-time performance with a balance between precision and speed.

• 🧠 Accuracy: Better object localization and class prediction.

• 📊 Versatility: Pretrained on the COCO dataset, making it a strong general-purpose model.

# YOLOv12 Performance Comparison: Latency vs. Accuracy and FLOPs vs. Accuracy 🎯

![Image](https://github.com/user-attachments/assets/d31e482c-6d5d-4271-932a-d042cc0ddc67)

# 📦 The COCO Dataset

The COCO (Common Objects in Context) dataset is a benchmark dataset in computer vision, containing 80 diverse classes such as:

• 🏃 Person

• 🚗 Car

• 🐕 Dog

• 📱 Cell phone

• 🍕 Pizza

Many more!

Instead of creating a custom dataset, I utilized COCO because it provides a rich set of labeled data that perfectly aligns with the needs of this project. Custom datasets are useful for domain-specific tasks, but COCO's versatility made it ideal for this general application.


# 🔧 How It Works

1. Live Video Feed 🎥: The system captures live video frames using OpenCV.

2. Object Detection 🧐: YOLOv12 processes each frame to detect objects and overlay bounding boxes.

3. Manual Object Selection 🖱️: Click on the object of interest, and the CSRT tracker initializes.

4. Tracking 🎯: The tracker updates the object's position frame by frame, ensuring dynamic tracking.

# 🚀 Technologies Used

• YOLOv12 for object detection.

• CSRT Tracker for robust object tracking.

• OpenCV for video processing and visualization.


#  🔗 Features

• Real-Time Processing: Instantaneous detection and tracking.

• Dynamic Tracking: Track any object selected in the live feed.

• Scalable: Can be extended to custom datasets if required.

• User-Friendly: Interactive and intuitive interface.


# 🛠️ How to Use

1. Clone the repository and ensure dependencies are installed.

2. Run the Python script.

3. Use the live video feed window to select an object by clicking on it.

4. Watch as the system tracks your selected object in real-time!


# Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/YOLOv12-Based_Object_Detection_and_Live-_Tracking-/blob/main/Demo.gif)
