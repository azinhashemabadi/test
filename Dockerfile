FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p /usr/src/app/staticfiles \
  && python manage.py collectstatic --noinput

CMD ["sh", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn config.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000"]

EXPOSE 8000
