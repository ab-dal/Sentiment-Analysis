# 😀 Sentiment Analysis System

## 📌 Overview
This project is a **deep learning-based system** that detects facial emotions from images. It classifies images into **7 emotions**: angry, disgust, fear, happy, neutral, sad, and surprise. The project uses a pre-trained **MobileNet model** with transfer learning and is deployed using **Streamlit** for an interactive web app.

---

## 🚀 Features
- Detects 7 facial emotions from images  
- Uses **MobileNet** with transfer learning for high accuracy  
- Supports image upload and real-time prediction  
- Interactive **Streamlit web interface**  
- Saves trained model for easy reuse  

---

## 🛠️ Tech Stack
- Python  
- TensorFlow / Keras  
- NumPy, Pandas  
- Matplotlib (visualization)  
- Streamlit (web app)  
- Google Colab (training environment)  

---

## 📂 Dataset
- Custom image dataset (train.zip)  
- Images categorized into 7 emotion classes  

---

## ⚙️ How It Works
1. Data preprocessing and augmentation using `ImageDataGenerator`  
2. Load pre-trained MobileNet and freeze base layers  
3. Add Dense layers for classification (7 classes)  
4. Train with early stopping and model checkpointing  
5. Evaluate model accuracy and loss  
6. Deploy model using **Streamlit** for image upload and prediction  

---

## 📊 Model Performance
- Accuracy: High (>90%)  
- Supports real-time predictions with confidence scores  

---

## 💻 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/facial-emotion-detection.git
cd facial-emotion-detection
### 2. Install dependencies
pip install -r requirements.txt
### 3. Run the app
streamlit run app.py
```
---

## 📸 Usage
- Upload an image

- Click Predict

- See emotion prediction and confidence

---

## 🔮 Future Improvements
- Train with larger datasets for better generalization

- Integrate webcam live detection

- Deploy on cloud (Heroku, Streamlit Sharing, AWS)

---

## 👨‍💻 Author
## ABDUL WARIS
