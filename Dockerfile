# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install --no-cache-dir Flask

# Expose port 80 to the outside world
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
