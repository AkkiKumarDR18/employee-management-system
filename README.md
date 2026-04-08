# 🏢 Employee Management System (EMS)

**Professional CRUD Application with Analytics Dashboard**

Developed as a technical assessment.  
This project follows a structured **Software Development Life Cycle (SDLC)** — from requirement analysis to a procedure-driven database architecture.

---

## 🚀 Key Features

- **Analytics Dashboard**  
  Real-time calculation of:
  - Total Workforce  
  - Monthly Payout  
  - Highest Salary  
  - Leading Department  
  (All powered by server-side aggregation)

- **Stored Procedure Architecture**  
  All CRUD operations are handled using **MySQL Stored Procedures** for:
  - Better performance  
  - Enhanced security  
  - Clean database abstraction  

- **Modern UI/UX**  
  Responsive admin portal built with:
  - Bootstrap  
  - Inter Font  
  - FontAwesome Icons  

- **Real-time Search**  
  Instant filtering of employees by:
  - Name  
  - Employee ID  
  - Department  
  *(No page reload required)*

- **Robust Error Handling**  
  Uses `try-except-finally` in Flask to:
  - Manage DB connections  
  - Show user-friendly flash messages  

---

## 🛠️ Technology Stack

| Layer      | Technology |
|-----------|----------|
| Backend   | Python 3, Flask |
| Database  | MySQL 8.0 |
| Frontend  | HTML5, CSS3, JavaScript |
| Libraries | flask-mysqldb, mysqlclient |

---

## 📊 Database Schema & Constraints

- **Salary Constraint**  
  ₹15,000 – ₹5,00,000 using SQL `CHECK`

- **Uniqueness Constraints**  
  - `emp_id`  
  - `email`  
  - `phone`

- **Stored Procedures**
  - `GetAllEmployees` → Fetch employees (latest first)  
  - `GetEmployeeStats` → Dashboard aggregation  
  - `AddEmployees` → Insert records  
  - `UpdateEmployee` → Update records  
  - `DeleteEmployee` → Remove records  

---

## ⚙️ Setup & Installation

### 1. Database Setup

Run the SQL script:

```sql
SOURCE path/to/database.sql;
```

### 2. Environment Setup

Run the following commands in your terminal to set up the Python environment:

#### Create a virtual environment (Optional but recommended)
```python
python -m venv venv
```

#### Activate the virtual environment

```bash
# On Windows:
venv\\Scripts\\activate

# On macOS/Linux:
source venv/bin/activate
```


#### Install required dependencies
```bash
pip install flask flask-mysqldb mysqlclient
```


### 3. Application Configuration

Update the app.config section in app.py with your local MySQL credentials:

```python
app.config\['MYSQL\_USER'] = 'your\_username'

app.config\['MYSQL\_PASSWORD'] = 'your\_password'
```

### 4. Running the Application
```bash
python app.py
```

Visit http://127.0.0.1:5000 in your web browser.


### 📸 Preview

<img width="1841" height="1027" alt="Screenshot 2026-04-08 130736" src="https://github.com/user-attachments/assets/69ab6851-23db-45e2-b1c3-da8108f1dd5f" />


## 📁 Project Structure

```bash
employee-system/

│

├── app.py              # Flask Application Logic

├── employee_db.sql        # SQL Schema & Stored Procedures

├── README.md           # Project Documentation

├── requirements.txt    # List of Dependencies

├── static/

│   ├── css/style.css   # Custom Modern Styling

│   └── js/script.js    # Search Filter Logic

└── templates/

│   └── index.html      # Main Template

```
