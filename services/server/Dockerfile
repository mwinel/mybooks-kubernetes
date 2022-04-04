# Base image
FROM python:3.7-slim

# Set working directory
WORKDIR /app

# Add and install required dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add app
COPY . /app

# Run server
CMD gunicorn -b 0.0.0.0:5000 manage:app
