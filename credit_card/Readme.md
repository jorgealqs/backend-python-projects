# 💳 Credit Card Approval System

## 📋 Overview

REST API system for credit card approval processing, built with Django REST Framework. The system evaluates credit card applications using machine learning algorithms to predict approval probability.

## 🚀 Quick Start

### Prerequisites

- Docker
- Docker Compose
- Git

### Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd credit_card
```

1.2 **Environment Setup**

```bash
cp .env.example .env
nano .env
```

1.3 **Build and Run**

```bash
docker-compose up --build
```

## 🛠 Project Structure

```textnote
credit_card/
├── api/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   └── tests/
├── core/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── ml_models/
│   └── credit_predictor.py
├── docker/
├── .env
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```

## 📚 API Documentation

### Endpoints

#### Credit Card Application

- `POST /api/v1/applications/` - Submit new application
- `GET /api/v1/applications/{id}/` - Get application status
- `GET /api/v1/applications/` - List all applications

#### Authentication

- `POST /api/v1/auth/token/` - Get authentication token
- `POST /api/v1/auth/refresh/` - Refresh token

## 🔧 Development

### Running Tests

```bash
docker-compose exec web python manage.py test
```

### Code Quality

```bash
# Run linting
docker-compose exec web flake8

# Run type checking
docker-compose exec web mypy .
```

## 🔐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DEBUG | Debug mode | True |
| SECRET_KEY | Django secret key | None |
| DB_NAME | Database name | credit_card_db |
| DB_USER | Database user | postgres |
| DB_PASSWORD | Database password | None |
| DB_HOST | Database host | db |
| DB_PORT | Database port | 5432 |

## 📦 Dependencies

- Django 4.2+
- Django REST Framework 3.14+
- PostgreSQL 13+
- Celery 5.3+
- Redis 5.0+

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors

### **Carlos ALberto Mendoza Cárdenas**

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&cacheBust=1)](https://www.linkedin.com/in/carlosalbertomc/)
- [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/526633312280?text=Hello%20Carlos,%20I'm%20interested%20in%20talking%20with%20you)

### **Jorge Alberto Quiroz Sierra**

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jorgealqs/)
- [![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:joralquisi@hotmail.com)
- [![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/573193662738?text=Hello%20Jorge,%20I'm%20interested%20in%20talking%20with%20you)

## 🙏 Acknowledgments

- Django Documentation
- Django REST Framework
- scikit-learn
