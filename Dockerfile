# Use a Python base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the requirements
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && python -m venv venv \
    && . venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the environment variables
ENV DISCORD_TOKEN=default
ENV OPENAI_API_KEY=default

# Set the entrypoint
CMD [ "venv/bin/python", "main.py" ]
