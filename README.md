# 🔐 Django REST Framework OTP Authentication API

> A secure, scalable, and lightweight **REST API** for One-Time Password (OTP) based user authentication built with **Django** and **Django REST Framework (DRF)**.

---

## 📌 Project Overview

This project provides a complete backend solution for user registration, login, and verification using One-Time Passwords (OTP). It includes custom user management, secure token handling, and modular app architecture for seamless integration into web and mobile applications.

---

## 🛠 Tech Stack

* **Language:** Python 3.x
* **Framework:** Django, Django REST Framework (DRF)
* **Database:** SQLite3 (Development) / PostgreSQL (Production)
* **Authentication:** OTP Verification (SMS / Email verification workflow)

---

## 🧩 Project Structure

```text
OTP/
├── apps/
│   └── accounts/          # User accounts, serializers, OTP logic & endpoints
├── app/                   # Core/Additional application logic
├── config/                # Main Django project settings & URL routing
├── db.sqlite3             # Local database
├── manage.py              # Django management script
└── req.txt                # Project dependencies
