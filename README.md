# 📝 Task Management API

A Django REST Framework (DRF) based API that allows users to **create tasks**, **assign tasks to users**, and **track assigned tasks**.

## 🚀 Features
- ✅ **Create Tasks** – Add new tasks with a name, description, and type.
- ✅ **Assign Tasks** – Assign tasks to one or multiple users.
- ✅ **Track Tasks** – Fetch tasks assigned to a specific user.
- ✅ **Swagger Documentation** – Interactive API documentation.
- ✅ **SQLite/PostgreSQL Support** – Uses Django ORM for database management.

---

## 🏠 Project Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/heygithub2606/Task_management_app.git
cd Task_management_app
```

### **2️⃣ Create and Activate Virtual Environment**
```bash
python -m venv env
```
- **For Windows:**
  ```bash
  env\Scripts\activate
  ```
- **For Mac/Linux:**
  ```bash
  source env/bin/activate
  ```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```bash
python manage.py migrate
```

### **5️⃣ Run the Development Server**
```bash
python manage.py runserver
```
API will be available at:  
👉 `http://127.0.0.1:8000/`

---

## 🛠️ API Endpoints

### **📌 Task Endpoints**
| Method | Endpoint | Description |
|--------|---------|------------|
| **POST** | `/api/tasks/create/` | Create a new task |
| **POST** | `/api/tasks/assign/` | Assign a task to users |
| **GET** | `/api/users/{user_id}/tasks/` | Get tasks assigned to a user |

### **📌 Request & Response Examples**

#### **1️⃣ Create a Task**
**📌 Request (`POST /api/tasks/create/`)**
```json
{
  "name": "Fix API Bug",
  "description": "Resolve the 500 error in the API",
  "task_type": "bug",
  "status": "pending",
  "assigned_users_ids": [1, 2]
}
```
**📌 Response (`201 Created`)**
```json
{
  "id": 1,
  "name": "Fix API Bug",
  "description": "Resolve the 500 error in the API",
  "task_type": "bug",
  "status": "pending",
  "assigned_users": [
    {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com",
      "mobile": "1234567890"
    },
    {
      "id": 2,
      "name": "Bob",
      "email": "bob@example.com",
      "mobile": "9876543210"
    }
  ]
}
```

#### **2️⃣ Assign a Task to Users**
**📌 Request (`POST /api/tasks/assign/`)**
```json
{
  "task_id": 1,
  "user_ids": [1, 2]
}
```
**📌 Response (`200 OK`)**
```json
{
  "message": "Task assigned successfully"
}
```

#### **3️⃣ Get Tasks Assigned to a User**
**📌 Request (`GET /api/users/1/tasks/`)**
```
GET http://127.0.0.1:8000/api/users/1/tasks/
```
**📌 Response (`200 OK`)**
```json
[
  {
    "id": 1,
    "name": "Fix API Bug",
    "description": "Resolve the 500 error in the API",
    "task_type": "bug",
    "status": "pending",
    "assigned_users": [
      {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "mobile": "1234567890"
      }
    ]
  }
]
```

---

## 📄 API Documentation (Swagger)
Once the server is running, you can access Swagger UI at:  
👉 **Swagger:** [`http://127.0.0.1:8000/swagger/`](http://127.0.0.1:8000/swagger/)  
👉 **ReDoc:** [`http://127.0.0.1:8000/redoc/`](http://127.0.0.1:8000/redoc/)  

---

## 🛠️ Technologies Used
- **Django** – Web framework
- **Django REST Framework (DRF)** – API development
- **SQLite/PostgreSQL** – Database
- **Swagger (`drf-yasg`)** – API documentation

---

## 🤝 Contributing
1. **Fork** the repository.
2. **Clone** the repository locally.
3. **Create a new branch**:  
   ```bash
   git checkout -b feature-new-task
   ```
4. **Commit changes**:  
   ```bash
   git commit -m "Added new feature"
   ```
5. **Push to GitHub**:  
   ```bash
   git push origin feature-new-task
   ```
6. **Create a Pull Request!** 🚀

---

## 💃 License
This project is licensed under the **MIT License**.

---

## 📩 Contact
For any questions or suggestions, feel free to reach out:  
📧 Email: [parulsha2606@gmail.com](mailto:parulsha2606@gmail.com)  
👤 GitHub: [heygithub2606](https://github.com/heygithub2606)  

