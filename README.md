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
├── app/
│   ├── main.py          # Entry point
│   ├── core/            # Config, settings
│   ├── auth/            # JWT, user auth
│   ├── products/        # Product & category routes
│   ├── cart/            # Cart endpoints
│   ├── orders/          # Order endpoints
│   ├── payments/        # Payment integration
│   └── models/          # SQLAlchemy models
├── tests/               # Unit & integration tests
├── requirements.txt
└── README.md
