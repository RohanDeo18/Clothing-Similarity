# Use a base image with Python 3.10.2
FROM python:3.10.2-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app

# Expose the port on which the application will run
EXPOSE 8080

# Set the entry point command to run the application
CMD ["python", "app.py"]