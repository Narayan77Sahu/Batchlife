# 🎓 BatchLife – Student Management System  

BatchLife is a hybrid desktop + web-based Student Management System built using **Python (Tkinter)** for the desktop interface and **Flask + MySQL** for backend and database management.

The project is designed to streamline student data handling, authentication, and academic record management with a clean UI and secure backend integration.

---

## 🚀 Tech Stack

### 🖥 Desktop Application
- Python
- Tkinter (GUI Framework)

### 🌐 Backend
- Flask (Python Web Framework)
- RESTful API Architecture

### 🗄 Database
- MySQL
- SQL Queries
- Relational Database Design

---

## ✨ Features

- 🔐 Secure Login & Registration System  
- 👨‍🎓 Student Record Management  
- ➕ Add / ✏ Update / ❌ Delete Student Data  
- 🔎 Search & Filter Students  
- 📊 Structured Database Storage  
- 🖥 Desktop GUI using Tkinter  
- 🌐 Flask Backend Integration  
- 🛡 Secure Database Connectivity  

---

## 📂 Project Structure

```

BatchLife/
│
├── gui/
│   ├── login.py
│   ├── dashboard.py
│   └── student_management.py
│
├── backend/
│   ├── app.py
│   ├── routes.py
│   └── database.py
│
├── database/
│   └── schema.sql
│
├── requirements.txt
└── README.md

````

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/batchlife.git
cd batchlife
````

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure MySQL Database

* Create a database in MySQL:

```sql
CREATE DATABASE batchlife;
```

* Update your database credentials in:

```python
database.py
```

### 5️⃣ Run Flask Backend

```bash
python app.py
```

### 6️⃣ Run Tkinter Application

```bash
python login.py
```

---

## 🔐 Authentication Flow

1. User registers through Tkinter GUI
2. Data stored securely in MySQL
3. Login credentials validated via Flask backend
4. On successful authentication → Dashboard access

---

## 🗄 Database Design

* Students Table
* Admin Table
* Academic Records
* Primary & Foreign Key Relationships
* Normalized Schema

---

## 🎯 Project Objectives

* Combine Desktop GUI with Web Backend
* Implement Secure Authentication System
* Manage Student Data Efficiently
* Apply Relational Database Concepts
* Build a Scalable Python-Based System

---

## 🛡 Security Implementation

* Password Hashing
* Input Validation
* Secure MySQL Queries
* Structured Backend API
* Error Handling Mechanism

---

## 📈 Future Enhancements

* 📊 Attendance Management
* 📅 Timetable Integration
* 📧 Email Notification System
* 📱 Web-based Dashboard
* 🔐 Role-Based Access (Admin/Student)
* 📦 Deployment on Cloud

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push to branch
5. Open Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developed By

**Deben Kumar Jena**
Python Developer | Flask Backend Developer | MySQL

---

⭐ If you like this project, consider giving it a star!

```

---

If you want, I can also:

- 🔥 Make it more **research-project style** (good for PRISM / academic submission)
- 📄 Add **system architecture diagram section**
- 🎯 Make it ATS-friendly for your resume
- 🌟 Make it look like a top GitHub trending repo**

Just tell me where you plan to use it 😎
```
