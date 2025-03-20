# Use an official Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . .
RUN pip install flask

# Command to run your Python app
CMD ["python", "app.py"]
