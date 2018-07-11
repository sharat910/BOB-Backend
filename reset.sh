rm db.sqlite3
rm -rf main/migrations/__pycache__
rm main/migrations/0001*.py
mv main/migrations/0002* main/migrations/backup/
python manage.py makemigrations
mv main/migrations/backup/0002* main/migrations
python manage.py migrate
#python manage.py createsuperuser
#python manage.py runserver
