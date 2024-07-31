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

# Copy the project files
COPY . /code/

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/code/entrypoint.sh"]
