
# 🛒 ETL Pipeline for E-Commerce Data

This project implements a complete ETL (Extract, Transform, Load) pipeline to collect and process e-commerce data from the [Fake Store API](https://fakestoreapi.com/). The data includes **products**, **users**, and **carts**, which are extracted, transformed, and loaded into JSON files and a TinyDB database.

---

## 📁 Project Structure

api_with_ia/
├── main.py # Entry point to run the ETL pipeline
├── etl/
│ ├── init.py
│ ├── extract.py # Extract data from the API
│ ├── transform.py # Clean and structure the data
│ └── load.py # Save the data to files and database
└── data/
├── products.json # Transformed product data
├── users.json # Transformed user data
└── carts.json # Transformed cart data



---

## ⚙️ Pipeline Overview

### 1. **Extract**
Data is retrieved from the public endpoints:
- `/products`
- `/users`
- `/carts`

### 2. **Transform**
- Fields are cleaned and filtered
- User names are joined and locations simplified
- Cart product listings are kept as-is

### 3. **Load**
- Transformed data is saved as `.json` files in `data/`
- A TinyDB database (`db.json`) is also updated

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
2. Run the pipeline
From the root folder:

python main.py
This will run the full ETL process and save the data to:


C:\Users\vitor\Desktop\api_with_ia\data
🧰 Dependencies
Python 3.8 or higher

requests

tinydb

Your requirements.txt should include:

shell
Copiar
Editar
requests>=2.31.0
tinydb>=4.7.1
📌 Features
Modular design (extract, transform, load)

Logs key ETL steps using logging

Error handling via try/except blocks

International-ready code (English-named variables and structure)

📈 Use Cases
Educational ETL demonstrations

E-commerce data simulation

Prototyping dashboards and analytics

📄 License
This project is open source and available under the MIT License.

👨‍💻 Author
Vitor
Feel free to connect on LinkedIn or reach out via email.
