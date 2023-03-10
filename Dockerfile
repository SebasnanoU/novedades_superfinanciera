# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations && python manage.py migrate
COPY . .
EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]