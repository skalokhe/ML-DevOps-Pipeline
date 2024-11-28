# Use Python 3.8 slim image
FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3
#setting variables 
ENV TF_ENABLE_ONEDNN_OPTS=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project to the container
COPY . .
# Ensure the models directory exists
RUN mkdir -p models

# Expose port 5000 for Flask app
EXPOSE 5000

# Run the Flask application
CMD ["python", "src/deployment/serve_model.py"]
