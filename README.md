<img width="1552" height="1168" alt="aifinder" src="https://github.com/user-attachments/assets/8d486f7f-57a5-409d-8618-52d43b154a96" />

---

<img width="2531" height="1221" alt="aifinderAdmin" src="https://github.com/user-attachments/assets/ba4b9dd1-2d25-42d0-9664-519f2a237101" />







# AI Finder

**AI Finder** is an AI tools discovery and directory platform built with Django and PostgreSQL.

The platform helps users discover, search, and explore different AI tools based on categories, target audiences, and pricing models.

Inspired by AI tools directories such as [Aixploria](https://www.aixploria.com/).

---

## Features

### Current Features

- Browse available AI tools
- View detailed information about each AI tool
- Search tools by name and description
- Filter tools by category
- Filter tools by target audience
- Filter tools by pricing model
- Combine multiple filters
- Sort tools by:
  - Newest
  - Oldest
  - Name (A–Z)
  - Name (Z–A)
  - Pricing
- Paginate search results
- View dedicated category pages
- View dedicated audience pages
- Display tool images
- Generate sample data using Django management commands

---

## Technology Stack

| Technology | Version |
|---|---|
| Python | 3.13 |
| Django | 5.2 |
| PostgreSQL | 18 |
| Faker | data generation |
| HTML / CSS | Frontend |
| Bootstrap | True |

---

## Project Structure

The project follows a modular Django architecture.

```text
AI-Finder/
│
├── apps/
│   ├── catalog/
│   │   ├── management/
│   │   │   └── commands/
│   │   │       └── seed_ai_tool.py
│   │   ├── models.py
│   │   ├── views.py
│   │   └── ...
│   │
│   └── taxonomy/
│       ├── models.py
│       └── ...
│
├── templates/
│   └── catalog/
│
├── media/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: This is a simplified representation of the project structure.*

---

## Requirements

Before installing the project, make sure you have the following software installed:

- Python 3.13
- PostgreSQL 18
- Git
- pip

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-finder.git

cd ai-finder
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt
```

If Faker is not already included in the requirements:

```bash
pip install Faker
```

### 4. Configure PostgreSQL

Create a PostgreSQL database for the project.

Open the PostgreSQL command-line tool or pgAdmin and execute:

```sql
CREATE DATABASE ai_finder;
```

Configure your database connection in the Django settings file.

Example database configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ai_finder",
        "USER": "YOUR_DB_USERNAME",
        "PASSWORD": "YOUR_DB_PASSWORD",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

Replace the username and password with your PostgreSQL credentials.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### 6. Generate Sample Data

AI Finder includes a custom Django management command for generating sample AI tools and related data.

Run:

```bash
python manage.py seed_ai_tool
```

This command generates sample records for development and testing.

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions to create an administrator account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

---

## Useful Django Commands

| Command | Description |
|---|---|
| `python manage.py runserver` | Start the development server |
| `python manage.py makemigrations` | Create database migrations |
| `python manage.py migrate` | Apply migrations |
| `python manage.py createsuperuser` | Create an administrator |
| `python manage.py shell` | Open Django shell |
| `python manage.py seed_ai_tool` | Generate sample data |
| `python manage.py check` | Check the project configuration |
| `python -m django --version` | Display Django version |

---

## Development Notes

- The project uses PostgreSQL as its primary database.
- Django applications are organized under the `apps/` directory.
- Sample data is generated using a custom management command.
- Uploaded images are stored in the media directory.
- Environment variables and sensitive configuration files should not be committed to Git.

---

## Roadmap

Planned features for future development:

- User authentication and profiles
- AI tool reviews and ratings
- Advanced search functionality
- More filtering options
- Favorites and bookmarks
- AI tool comparison
- Admin dashboard improvements
- SEO optimization
- REST API
- Responsive UI improvements

---

## Contributing

Contributions, suggestions, and bug reports are welcome.

If you find an issue or have an idea for improvement, feel free to open an issue or submit a pull request.

---

## License

This project is currently under development. A license has not yet been selected.

