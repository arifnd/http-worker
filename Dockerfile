# Use the official Python image as the parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 8080 to the host
EXPOSE 8080

# Start the application
CMD ["python", "app.py"]
