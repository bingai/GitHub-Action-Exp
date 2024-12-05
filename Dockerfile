# Use slim Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
COPY src/ ./src/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command
CMD ["python", "-m", "src.addition"]