# 🛒 FastAPI E-commerce API

A modern **E-commerce REST API** built with [FastAPI](https://fastapi.tiangolo.com/).  
This project provides a backend foundation for an online store, including **products, categories, cart, orders, authentication, and payment integration**.

---

## 🚀 Features

- 🔐 **JWT Authentication** (register, login, role-based access: admin vs customer)
- 📦 **Product Management** (CRUD for products & categories)
- 🛒 **Cart System** (add, update, remove items)
- 🧾 **Order Management** (checkout, order tracking, admin updates)
- 💳 **Payment Integration Ready** (Stripe, Paystack, Flutterwave, etc.)
- 📄 **Auto-generated API Docs** with Swagger & ReDoc
- ⚡ **Fast & Async** using FastAPI
- 🛠️ **Modular Project Structure** for scalability

---

## 📂 Project Structure

```bash
ecommerce-api-fastapi/
├── README.md
├── __init__.py
├── api
│   ├── __init__.py
│   └── v1
│       ├── __init__.py
│       ├── models
│       │   └── __init__.py
│       ├── routes
│       │   └── __init__.py
│       ├── schemas
│       │   └── __init__.py
│       ├── services
│       │   └── __init__.py
│       └── utils
│           └── __init__.py
├── app.py
├── requirements.txt
└── utils
    ├── __init__.py
    └── dependencies.py
