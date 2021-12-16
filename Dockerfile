# This Dockerfile fixes Railway deployment
# Heroku deployment doesn't use this
# Thanks to https://t.me/aishiktokdar

FROM python:3.9-slim

WORKDIR /app
RUN chmod 777 /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "script.py"]
