# Use a slim Python image
FROM python:3.9-slim

# Install build dependencies and MySQL client libraries
RUN apt-get update && apt-get install -y \
    pkg-config \
    libmariadb-dev \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies (including mysqlclient)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .
# Copy wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
