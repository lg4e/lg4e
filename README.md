<<<<<<< HEAD
 LG4E - Local Deployment Guide (Linux)

This guide describes how to deploy the [LG4E](https://github.com/lg4e/lg4e.git) project locally on a Linux system.

---

## 🚩 Prerequisites

- **Python 3.8+**
- **Git**
- Virtual environment tool (`venv` recommended)
- Ubuntu or other Linux distribution

---

## ⚙️ Deployment Steps

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/lg4e/lg4e.git
cd lg4e
```

### 2. Create and Activate a Virtual Environment

Use Python’s built-in virtual environment tool:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Within the activated virtual environment:
```bash
pip install -r requirements.txt
```

### 4. Run the Local Development Server

Start the Flask development server:
```bash
python app.py
```

Visit your application in the browser at:
http://localhost:5000
=======
 LG4E - Local Deployment Guide (Linux)

This guide describes how to deploy the [LG4E](https://github.com/lg4e/lg4e.git) project locally on a Linux system.

---

## 🚩 Prerequisites

- **Python 3.8+**
- **Git**
- Virtual environment tool (`venv` recommended)
- Ubuntu or other Linux distribution

---

## ⚙️ Deployment Steps

### 1. Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/lg4e/lg4e.git
cd lg4e
```

### 2. Create and Activate a Virtual Environment

Use Python’s built-in virtual environment tool:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Within the activated virtual environment:
```bash
pip install -r requirements.txt
```

### 4. Run the Local Development Server

Start the Flask development server:
```bash
python app.py
```

Visit your application in the browser at:
http://localhost:5000
>>>>>>> c52572e (Update descriptions)
