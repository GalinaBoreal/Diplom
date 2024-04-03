FROM python:3.10.0-alpine

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

RUN python3 manage.py migrate --run-syncdb

CMD python3 manage.py runserver 0.0.0.0:8000