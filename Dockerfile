# Use official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for the app
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
