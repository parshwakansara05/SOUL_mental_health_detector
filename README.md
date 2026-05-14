# SOUL — Supportive Observer for User's Well Being  Life

## Overview

SOUL (Supportive Observer for User’s Life) is an AI-powered mental health analysis web application that predicts whether a user may require mental health support based on lifestyle, emotional, and behavioral inputs.

The project uses Machine Learning with a Flask backend to analyze user responses and provide intelligent predictions in a clean and interactive web interface.

---

# Features

* Mental health prediction using Machine Learning
* Interactive and responsive UI
* Flask backend integration
* Real-time prediction system
* Clean frontend with animations and modern design
* Encoded categorical input handling
* Error handling for unseen labels
* JSON-based API communication

---

# Tech Stack

## Frontend

* Figma - Coverted to HTML and CSS Using MCP

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

---

# Project Structure

```bash
SOUL/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── template/
│   ├── soul-landing.html
│   └── soul-analyzer.html
│
├── app.py
├── soul_model.pkl
├── label_encoders.pkl
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/SOUL.git
cd SOUL
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Application

```bash
python app.py
```

Server will start on:

```bash
http://127.0.0.1:5000/
```

---

# Machine Learning Workflow

1. Dataset preprocessing
2. Label encoding categorical data
3. Model training using Scikit-learn
4. Saving model using Pickle
5. Flask API integration
6. Frontend prediction visualization

---

# Input Parameters

The model analyzes multiple behavioral and emotional factors such as:

* Gender
* Occupation
* Self Employment Status
* Family Mental Health History
* Days Indoors
* Stress Level
* Habit Changes
* Mental Health History
* Mood Swings
* Coping Struggles
* Work Interest
* Social Weakness

---

# Prediction Output

The system predicts whether the user may:

* Need Mental Health Treatment
* Not Require Immediate Treatment

---

# Future Improvements

* AI chatbot integration
* Voice-based mental health analysis
* Emotion detection using facial expressions
* Real-time counseling recommendations
* User authentication system
* Database integration
* Dashboard analytics

---

# Requirements

```txt
Flask
pandas
numpy
scikit-learn
pickle-mixin
```

---

# Author

## Parshwa Kansara

AI & ML Engineering Student

Passionate about building intelligent systems using Artificial Intelligence, Machine Learning, and modern web technologies.

---
