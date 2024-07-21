# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to non-interactive
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system packages
RUN apt-get update && \
    apt-get install -y wget gnupg curl unzip && \
    rm -rf /var/lib/apt/lists/*

# Install Microsoft Edge
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/microsoft-prod.list && \
    apt-get update && \
    apt-get install -y microsoft-edge-stable

# Install Microsoft Edge WebDriver
RUN EDGE_VERSION=$(microsoft-edge --version | awk '{print $3}') && \
    wget -O /tmp/edgedriver.zip "https://msedgedriver.azureedge.net/${EDGE_VERSION}/edgedriver_linux64.zip" && \
    unzip /tmp/edgedriver.zip -d /usr/local/bin && \
    rm /tmp/edgedriver.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Run the script
CMD ["python", "your_script.py"]
