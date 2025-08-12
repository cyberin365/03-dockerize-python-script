FROM python:3-slim

# make a folder alongside the system folders such as bin, etc, usr,
# but specifically for our application code
WORKDIR /workspace

# Install only necessary system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into container
COPY trivialScript.py .

# Set environment variables
ENV MAX_ROWS=10
ENV RANDOM_SEED=42

# Command to run the application
CMD ["python", "trivialScript.py"]