# Use Python 3.8 slim image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "src/deployment/serve_model.py"]