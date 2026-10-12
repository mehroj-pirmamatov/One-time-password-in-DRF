# 🔐 OTP Verification Service

A secure, high-performance API service for generating, sending, and verifying One-Time Passwords (OTP) with rate limiting and expiration management.

---

## ✨ Features

- 🎲 **Secure OTP Generation:** Generates cryptographically secure numeric/alphanumeric codes.
- ⏱️ **Time-based Expiration:** Configurable TTL (Time-To-Live) for generated OTPs.
- 🛑 **Rate Limiting & Brute-force Protection:** Prevents spamming and unauthorized verification attempts.
- 📩 **Multi-channel Delivery:** Support for sending OTPs via SMS, Email, or Messaging platforms (Telegram).
- 🔄 **Auto-cleanup:** Automatic removal of expired or used tokens (via Redis/Celery).

---

## 🛠️ Tech Stack

- **Language:** Python
- **Framework:** Django / Django REST Framework (yoki FastAPI)
- **Database:** PostgreSQL / Redis
- **Task Queue:** Celery

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/username/otp-service.git](https://github.com/username/otp-service.git)
   cd otp-service
