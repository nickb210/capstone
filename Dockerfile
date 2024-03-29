FROM python:3.8-alpine

# Expose port 80
EXPOSE 80/tcp


RUN mkdir /code
WORKDIR /code

# Copy requirements.txt to WORKDIR
COPY requirements.txt .

RUN apk add build-base

# Install requirements from flask_sms.py
RUN pip install -r requirements.txt

# Copy flask_sms.py to WORKDIR
COPY code .

# Run flask_sms.py application
#CMD ["python", "app.py"]
ENTRYPOINT python app.py