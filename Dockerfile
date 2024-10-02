# Use the latest Python image
FROM python:3.9-slim

LABEL maintainer="Hussein Ali"

# Set the working directory and environment variables
ENV APP_HOME /app
WORKDIR $APP_HOME

# Create a non-root user for security
RUN useradd -m -d /home/pythonuser pythonuser && usermod -aG root pythonuser

# Switch to the non-root user
USER pythonuser

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY . .

# Ensure Gauge is installed globally and set up
RUN gauge install python

# Run the tests using Gauge with tags and retry options
#CMD ["gauge", "run", "--tags", "Tag_Name", "--max-retries-count=3", "specs"]

# Run the tests with max retry set to 3
CMD ["gauge", "run", "--max-retries-count=3", "specs"]