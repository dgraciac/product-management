# product-management

Install Python 3.12


Create a virtual environment: `python3.12 -m venv .venv`

Activate it: `source .venv/bin/activate`

Install dependencies: `pip install -r requirements.txt`

Run server: `python manage.py runserver`

Make migrations example: `python manage.py makemigrations polls`

Run migrations: `python manage.py migrate`

You can deactivate a virtual environment with: `deactivate`

Back office: `/admin/`

Superuser:
- admin
- admin@example.com
- password