FROM python:3.7.7
LABEL maintainer="chauhanchetan82@gmail.com"

COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
