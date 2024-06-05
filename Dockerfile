# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN apt-get update -q && \
    apt-get install -y \
    libgirepository1.0-dev \
    dbus \
    dbus-x11 \
    dbus-user-session \
    libdbus-1-dev && \
    pip3 install -r requirements.txt

# Run script when the container launches
#CMD ["python", "pm.py"]

