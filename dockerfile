# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install system dependencies (you might need to add more depending on your requirements)
# Adding a retry loop to handle temporary network connectivity issues.
# Also, consider using a different Debian mirror if deb.debian.org is not reachable from your network.
RUN for i in {1..5}; do apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libc6-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* && break || sleep 5; done

# Update pip and install any needed packages specified in requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -vvv -r requirements.txt

COPY ./data /usr/src/app/data

# Make sure the entrypoint.sh script is executable
RUN chmod +x /usr/src/app/entrypoint.sh

# Set the entrypoint script to be executed when the container starts
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Your service runs on port 8000 by default, expose it
EXPOSE 8000

# Run the application
CMD ["python", "/usr/src/app/main.py"]