# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file to the container
COPY ..

# Install the dependencies in the container
RUN pip install django==3.2
#--no-cache-dir -r requirements.txt

# Copy the main file to the container
#COPY CliCalculator.py

# Set the entrypoint to run the main file
ENTRYPOINT ["python", "CliCalculator.py"]
