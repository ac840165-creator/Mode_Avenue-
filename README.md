# Mode Avenue - E-Commerce Storefront

Mode Avenue is a full-featured, responsive fashion e-commerce storefront built with **Flask (Python)** and **SQLite**. It supports user profiles, shopping carts, order checkouts, PDF invoice generation, and a complete administrator dashboard.

## 🚀 How to Run the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/ac840165-creator/Mode_Avenue-.git
cd Mode_Avenue-
```

### 2. Set up a Virtual Environment
```bash
python -m venv venv
```
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python run.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

## 🔐 Credentials for Testing

### Admin Dashboard Access
- **URL**: `http://127.0.0.1:5000/admin/admin_login`
- **Email**: `ac840165@gmail.com`
- **Password**: `admin123`

## 🛠️ Technology Stack
- **Backend**: Python (Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-WTF)
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, Bootstrap 5, FontAwesome
- **PDF Invoices**: ReportLab
