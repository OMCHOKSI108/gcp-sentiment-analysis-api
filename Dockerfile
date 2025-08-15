# Use an official, slim Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# Install dependencies and download TextBlob corpora
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora

# Copy the rest of the application code into the container
COPY . .

# Set the command to run the application using Gunicorn, a production-grade server
# It listens on the port specified by the PORT environment variable, which Cloud Run provides.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app