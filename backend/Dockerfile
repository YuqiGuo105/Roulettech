# Use the official Python image from the Docker Hub
FROM python:3.9-slim

LABEL author="yuqi.guo17@gmail.com"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project code
COPY . /code/

# Expose port 8001
EXPOSE 8001

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
