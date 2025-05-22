# retail_data_pipeline_with_ai

📄 README.md

# 🛒 ETL Pipeline for E-Commerce Data

This project implements a complete ETL (Extract, Transform, Load) pipeline for consuming and processing e-commerce data from [Fake Store API](https://fakestoreapi.com/). The data includes **products**, **users**, and **carts**, which are extracted, transformed, and loaded into local JSON files and a TinyDB database.

---

## 📦 Project Structure

api_with_ia/
├── main.py # Entry point to run the ETL pipeline
├── etl/
│ ├── init.py
│ ├── extract.py # Data extraction from public API
│ ├── transform.py # Data cleaning and transformation
│ └── load.py # Load transformed data into JSON and TinyDB
└── data/
├── products.json # Transformed product data
├── users.json # Transformed user data
└── carts.json # Transformed cart data


---

## ⚙️ How It Works

### 1. **Extract**
- Fetches data from:
  - `/products`
  - `/users`
  - `/carts`

### 2. **Transform**
- Products: Only relevant fields are kept (id, title, price, etc.)
- Users: Names are concatenated, only relevant address info is retained
- Carts: Filters necessary cart-related fields

### 3. **Load**
- Stores the transformed data into:
  - JSON files located at `C:\Users\vitor\Desktop\api_with_ia\data`
  - TinyDB database at the same location

---

## 🚀 How to Run

1. **Clone this repository** or download the files.

2. Make sure you have the required dependencies:
   ```bash
   pip install requests tinydb
Run the pipeline from the project root:


cd C:\Users\vitor\Desktop\api_with_ia
python main.py
🧰 Dependencies
Python 3.8+

Requests

TinyDB

To install:


pip install -r requirements.txt
📁 Output Location
All output files are saved in:

C:\Users\vitor\Desktop\api_with_ia\data
Includes:

products.json

users.json

carts.json

db.json (TinyDB)

🛡️ Error Handling and Logging
All ETL operations are wrapped with try/except blocks and use Python’s logging module. Logs are printed to the console and may optionally be redirected to a file for production.

📈 Potential Use Cases
Testing or simulating e-commerce data flows

Teaching ETL concepts

Building dashboards from structured data

Prototyping analytics or AI on retail datasets

✨ Author
Vitor
📧 Contact: [Your Email or LinkedIn]
