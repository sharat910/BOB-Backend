rm db.sqlite3
rm -rf main/migrations/__pycache__
rm main/migrations/000*.py
python manage.py makemigrations
python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver
