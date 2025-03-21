# FreebieProject
# **Freebie Tracker**  

## **Project Overview**  
The **Freebie Tracker** is a Python-based application that allows developers to track the freebies (swag) they receive from companies at hackathons or events.  

The project is built using **SQLAlchemy** for database management and **Alembic** for handling migrations.  

---

## **📌 Features**  
- **Company Management**: Track different companies and their founding years.  
- **Developer Management**: Keep records of developers who receive freebies.  
- **Freebie Tracking**: Maintain a list of freebies, their values, and which developer received them.  
- **CRUD Operations**: Create, Read, Update, and Delete records using SQLAlchemy.  
- **Database Relationships**: Establish a **many-to-many** relationship between developers and companies through freebies.  

---

## **📌 Technologies Used**  
- **Python**  
- **SQLAlchemy (ORM)**  
- **SQLite (Database)**  
- **Alembic (Migrations)**  

---

## **📌 Installation & Setup**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/FreebieTracker.git
cd FreebieTracker
```

### **2️⃣ Set Up a Virtual Environment**  
```sh
pipenv install
pipenv shell
```

### **3️⃣ Initialize the Database**  
```sh
alembic upgrade head
```

### **4️⃣ Seed the Database with Sample Data**  
```sh
python seed.py
```

### **5️⃣ Run Debugging Mode**  
```sh
python debug.py
```

---

## **📌 Database Schema**  

| **Table**     | **Columns**                           | **Relationships**                            |
|--------------|--------------------------------|--------------------------------|
| `companies`  | `id`, `name`, `founding_year` | One-to-Many with `freebies`   |
| `devs`       | `id`, `name`                 | One-to-Many with `freebies`   |
| `freebies`   | `id`, `item_name`, `value`, `company_id`, `dev_id` | Many-to-One with `companies` and `devs` |

---

## **📌 Available Methods**  

### **🔹 Freebie Methods**
- `print_details()` → Returns a formatted string: `{dev_name} owns a {item_name} from {company_name}`  

### **🔹 Company Methods**
- `give_freebie(dev, item_name, value)` → Assigns a freebie to a developer  
- `oldest_company()` → Returns the company with the **earliest founding year**  

### **🔹 Developer Methods**
- `received_one(item_name)` → Checks if the developer received a specific item  
- `give_away(dev, freebie)` → Transfers a freebie to another developer  

---

## **📌 How to Use**  

### **1️⃣ Open Debug Mode**
```sh
python debug.py
```

### **2️⃣ Run Sample Queries**
Inside the interactive session:
```python
# Fetch Oldest Company
Company.oldest_company()

# Check if a Developer Received a Specific Freebie
alice.received_one("T-shirt")

# Transfer a Freebie from Alice to Bob
alice.give_away(bob, f1)
```

---

## **📌 Contribution**  
If you'd like to contribute:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-branch`).  
3. Commit changes (`git commit -m "Add new feature"`).  
4. Push to GitHub (`git push origin feature-branch`).  
5. Open a pull request.  

---
