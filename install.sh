python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python3 manage.py runserver 0.0.0.0:8000
