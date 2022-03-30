# Base image
FROM python:3.7-slim

ENV PORT 5000

# Install netcat
RUN apt-get update && \
    apt-get -y install netcat && \
    apt-get clean

# Set working directory
WORKDIR /app

# Add and install required dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Add entrypoint.sh
# COPY ./entrypoint.sh /app/entrypoint.sh
# RUN chmod +x /app/entrypoint.sh

# Add app
COPY . /app

# Run server
# CMD ["/app/entrypoint.sh"]
# ENTRYPOINT [ "/app/entrypoint.sh" ]
CMD gunicorn -b 0.0.0.0:5000 manage:app
