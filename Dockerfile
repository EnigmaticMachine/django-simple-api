FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set work directory
WORKDIR /code

# Install pip
RUN pip install --upgrade pip

# Copy only requirements to cache dependencies layer
COPY requirements.txt /code/

# Install project dependencies
RUN pip install -r /code/requirements.txt

# Copy only the necessary project files
COPY manage.py /code/
COPY /scripts/entrypoint.sh /code/entrypoint.sh

# Copy backend and core applications
COPY config /code/config
COPY api /code/api

# Copy settings and tests
COPY settings /code/settings

# Ensure entrypoint script is executable
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]
