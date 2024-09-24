FROM python:3.10-slim

WORKDIR /app

COPY ./netbox/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./netbox .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]