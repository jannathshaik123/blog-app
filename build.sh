set -o exit

pip install requirements.txt

pyrhon manage.py collectstatic --noinput
python manage.py migrate