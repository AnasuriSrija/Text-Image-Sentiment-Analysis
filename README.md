# Text-Image Sentiment Analysis

A web application that combines image and text features to identify image content and detect sentiment using deep learning.

## Features

* Fusion of visual and textual data for accurate sentiment classification
* Convolutional Neural Network (CNN) backbone with CTC decoding for sequence prediction
* Intuitive web interface powered by JSP and Flask
* Lightweight SQLite database for data storage

## Tech Stack

* **Backend**: Python, Flask, TensorFlow
* **Frontend**: JavaServer Pages (JSP), HTML/CSS, JavaScript
* **Data Processing**: NumPy, Pandas
* **Database**: SQLite

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/AnasuriSrija/Text-Image-Sentiment-Analysis.git
   cd Text-Image-Sentiment-Analysis
   ```
2. **Create a Python virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize the database**

   ```bash
   python init_db.py
   ```
5. **Run the server**

   ```bash
   python app.py
   ```
6. **Access the application**
   Open your browser at `http://localhost:5000`.

## Usage

* Upload an image containing text or graphics via the web form.
* The CNN model extracts visual features, converts them into sequences, and decodes them with CTC.
* Combined with extracted text features, the system outputs the detected sentiment.

## Project Structure

```
├── app.py            # Flask application entry point
├── init_db.py        # Database setup script
├── model/            # CNN model code and weights
├── templates/        # JSP files and web assets
├── static/           # CSS, JavaScript, images
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

