# 🛒 E-Commerce ETL Pipeline

This project is a modular **ETL pipeline** (Extract, Transform, Load) that collects e-commerce data from a public API and stores it locally in both JSON files and a TinyDB database.

---

## 📦 What It Does

- 🔄 **Extracts** data from [Fake Store API](https://fakestoreapi.com/)
- 🧹 **Transforms** product, user, and cart data into clean formats
- 💾 **Loads** the processed data into:
  - JSON files
  - TinyDB (NoSQL local database)

---

## 🗂️ Project Structure

```text
api_with_ia/
├── ai
├── main.py               # Entry point for running the pipeline
├── etl/                  # ETL logic lives here
│   ├── extract.py        # Extracts data from API
│   ├── transform.py      # Transforms raw data
│   └── load.py           # Loads data into files and database
├── data/                 # Output folder for processed data
    ├── carts.json        # carts storage file
    ├── product.json      # product storage file
    ├── tinydb.json       # TinyDB storage file
    └── users.json        # users storage file
├── tests/
│   ├── products.json
│   ├── users.json
│   └── carts.json
├── etl_log.log
├── db.json               # TinyDB storage file
└── requirements.txt      # Dependencies
```
---

## 🚀 How to Run

1. **Install dependencies**

---

```bash
pip install -r requirements.txt
Run the ETL pipeline```


python main.py
The data will be saved to:



And also stored in db.json using TinyDB.

---

🔧 Technologies Used
Python 3.8+

requests

tinydb

---

✅ Features
Modular ETL architecture

Error handling with try/except blocks

Logging with timestamps and levels

Organized for international development

Easily extensible

---

📊 Use Case
This project is ideal for:

Learning ETL architecture

Prototyping analytics pipelines

Simulating data pipelines for e-commerce

---

📝 License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

👨‍💻 Author
Developed by Enock.
Feel free to connect on LinkedIn or send a message via email.
LinkedIn :https://www.linkedin.com/in/joao-victor-enock-972b682b9/
Gmail: enokjoao@gmail.com

