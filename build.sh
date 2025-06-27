set -o errexit

pip install -r requirements.txt

pyrhon manage.py collectstatic --no-input
python manage.py migrate