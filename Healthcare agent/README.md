# 🏥 Healthcare AI Agent

A simple AI-powered healthcare assistant built using **Flask (Backend)**
and **HTML/CSS/JS (Frontend)**.

------------------------------------------------------------------------

## 🚀 Features

-   Accepts user symptoms from the UI\
-   Sends them to Flask backend API\
-   Returns AI-generated response\
-   Clean UI layout\
-   Fully CORS-enabled\
-   Easy to deploy anywhere

------------------------------------------------------------------------

## 🧩 System Architecture (Diagram)

``` mermaid
flowchart TD
    A[User in Browser] --> B[Frontend HTML/CSS/JS]
    B --> C[POST /ask API]
    C --> D[Flask Backend]
    D --> E[Generate Response]
    E --> B
```

------------------------------------------------------------------------

## 📁 Project Structure

    Healthcare-agent/
    │── app.py
    │── README.md
    │── index.html
    │── script.js
    │── styles.css

------------------------------------------------------------------------

## 🛠️ Installation Instructions

### **1️⃣ Install Python**

Download Python from: https://www.python.org/

Ensure Python is added to PATH.

------------------------------------------------------------------------

### **2️⃣ Install Flask & CORS**

Open terminal:

``` bash
pip install flask flask-cors
```

------------------------------------------------------------------------

### **3️⃣ Run the Backend**

Navigate to your project folder:

``` bash
cd Healthcare-agent
python app.py
```

If successful, you will see:

     * Running on http://127.0.0.1:5000

------------------------------------------------------------------------

### **4️⃣ Run Frontend (HTML)**

Right‑click **index.html** → **Open with Live Server**\
(or simply open the file in browser)

Now your UI appears at something like:

    http://127.0.0.1:5500/index.html

------------------------------------------------------------------------

## 🔌 API Endpoint Description

### **POST /ask**

**Request:**

``` json
{
  "question": "I have fever and headache"
}
```

**Response:**

``` json
{
  "answer": "Received symptom: I have fever and headache"
}
```

------------------------------------------------------------------------

## 🌐 Deployment Guide (GitHub Pages + Backend)

GitHub Pages can host only the **frontend**.\
Backend (Flask) must be deployed on:

-   Render\
-   Railway\
-   Vercel (Python serverless)\
-   AWS / Azure

### **Deploy Frontend to GitHub Pages**

1.  Create GitHub repo\
2.  Upload:
    -   index.html\
    -   script.js\
    -   styles.css\
3.  Go to: **Settings → Pages**\
4.  Set:
    -   Source → `main` branch\
    -   Folder → `/ (root)`\
5.  Save → GitHub gives you a public website URL

### **Update API URL in script.js**

Replace:

``` js
fetch("http://127.0.0.1:5000/ask")
```

With your deployed backend API URL.

------------------------------------------------------------------------

## 🧪 Testing

-   Use browser console (F12 → Console)
-   Test API using Postman or Curl


------------------------------------------------------------------------


