# Use Python 3.11 slim from GitHub Container Registry
FROM ghcr.io/python/python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY app.py .

# Command to run app
CMD ["python", "app.py"]
