 #video 43+45
# start docker kernal + python
# Use the official Python image from Docker Hub based on a slim version of Debian Bullseye # https://hub.docker.com/_/python
FROM python:3.11.11-slim-bullseye

# Enable unbuffered output for Python (helps with logging)
ENV PYTHONUNBUFFERED 1

# Update package lists and install necessary system dependencies (e.g., GCC, PostgreSQL client libraries)
RUN apt-get update && apt-get -y install gcc libpq-dev

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container's /app directory
COPY requirements.txt /app/requirements.txt

# Install Python dependencies from the requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the entire project directory to the /app folder inside the container
COPY . /app/

# Optionally, you can expose a port if your app requires it (e.g., for web apps)
# EXPOSE 8000

# Command to run the application (if you have an entrypoint or specific start command)
# CMD ["python", "app.py"]  # Replace with your app's start command, e.g., a Flask/Django app

