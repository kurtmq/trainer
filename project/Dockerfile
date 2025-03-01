# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=project.settings_prod

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

<<<<<<< HEAD
# Run migrations and run gunicorn
CMD python manage.py migrate && gunicorn --bind 0.0.0.0:$PORT project.wsgi
=======
# Run gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT project.wsgi:application
>>>>>>> 0b5876ce6fbda13563726d20e9196e48eae2b7dc
