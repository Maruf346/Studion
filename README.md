# Studion
**Practical online courses, structured for real skills.**

Studion is a modern, full-stack online course platform that allows users to browse, purchase, and access high-quality online courses. Designed for scalability and maintainability, Studion provides a clean architecture and secure payment and authentication mechanisms. Currently, only admins can post and manage courses, ensuring quality content.

---

## Features

- **User Authentication**
  - Google OAuth for secure login
  - JWT-based authentication for API access

- **Course Management**
  - Admin-only course creation
  - Structured courses with sections and lessons
  - Support for text, video, and document content

- **Payment Integration**
  - SSLCommerz payment gateway for secure course purchases
  - Track transaction history and payment status

- **User Dashboard**
  - View purchased courses
  - Access lessons securely
  - Progress tracking (optional for future versions)

- **API-first Architecture**
  - Built with Django REST Framework
  - Ready for React or Next.js frontend integration

- **Scalable & Maintainable**
  - Modular Django apps: accounts, courses, payments, enrollments, core
  - Clean folder structure for easy development and expansion

---

## Tech Stack

- **Backend:** Python, Django, Django REST Framework  
- **Frontend:** React / Next.js (planned)  
- **Database:** PostgreSQL (or MySQL)  
- **Authentication:** Google OAuth + JWT  
- **Payments:** SSLCommerz  
- **Deployment:** Vercel (frontend), VPS / Cloud Server (backend)  

---



## Getting Started

### Prerequisites

* Python 3.11+
* PostgreSQL or MySQL
* pip
* Node.js & npm (for frontend integration)
* Google OAuth credentials
* SSLCommerz sandbox/live account (for payments)

### Installation

1. Clone the repository

```bash
git clone https://github.com/Maruf346/Studion.git
cd Studion/Backend
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Setup database

```bash
# Example for PostgreSQL
createdb studion_db
python manage.py migrate
```

5. Create superuser (admin)

```bash
python manage.py createsuperuser
```

6. Run development server

```bash
python manage.py runserver
```

Access backend at: `http://127.0.0.1:8000/`

---

## Future Plans

* Frontend integration with Next.js for SSR & SEO
* Course progress tracking & certificates
* Batch management for live classes
* Enhanced analytics & reporting for admins

---

## License

This project is open-source and free to use under the MIT License.

---

## Contact

For questions or contributions:

* GitHub: [https://github.com/yourusername/studion-backend](https://github.com/Maruf346/Studion)
* Email: [your.email@example.com](mailto:maruf.bshs@gmail.com)

