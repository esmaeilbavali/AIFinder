# AI Finder

AI Finder is a directory of AI tools designed to help users discover and explore artificial intelligence tools based on their categories, target audiences, pricing models, and features.

The project provides both a Django-based web interface and a RESTful API.

## Features

- Browse AI tools
- View detailed information about each tool
- Search tools by name and description
- Filter tools by category, audience, and pricing type
- Combine multiple filters
- Sort tools by different fields
- Paginate tool listings
- Browse tools by category and audience
- Display tool images
- Seed the database with sample data using Faker
- Read-only REST API built with Django REST Framework
- API documentation with Swagger UI and ReDoc

## Technology Stack

| Technology | Version / Usage |
|---|---|
| Python | 3.12+ |
| Django | 6.1.3 |
| Django REST Framework | 3.18.3 |
| drf-spectacular | 0.30.0 |
| SQLite | Development database |
| Faker | Sample data generation |
| Pillow | Image processing |
| Bootstrap | Frontend styling |

## Project Structure

```text
AIFinder/
├── apps/
│   ├── api/
│   │   ├── serializers/
│   │   ├── views/
│   │   ├── filters.py
│   │   ├── pagination.py
│   │   └── urls.py
│   ├── catalog/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_ai_tool.py
│   │   ├── models.py
│   │   ├── selectors.py
│   │   ├── services.py
│   │   ├── urls.py
│   │   └── views.py
│   └── taxonomy/
│       ├── models.py
│       └── ...
├── config/
│   ├── settings.py
│   └── urls.py
├── templates/
├── static/
├── media/
├── manage.py
├── requirements.txt
├── .env-example
└── README.md
```

## Requirements

- Python 3.12 or newer
- pip
- Git

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:esmaeilbavali/AIFinder.git
cd AIFinder
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create your local `.env` file from the example:

```bash
cp .env-example .env
```

Generate a new Django secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Set the generated key as the value of `SECRET_KEY` in `.env`.

The project currently uses SQLite as its database. PostgreSQL environment variables are included as placeholders for possible future configuration.

**Important:** Never commit your actual `.env` file or expose your secret key.

### 5. Apply migrations

```bash

## Screenshots

![AI Finder Homepage](https://github.com/user-attachments/assets/8d486f7f-57a5-409d-8618-52d43b154a96)

![AI Finder Admin](https://github.com/user-attachments/assets/ba4b9dd1-2d25-42d0-9664-519f2a237101)
