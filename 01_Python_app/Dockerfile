# 1. Start with an existing Python environment
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependency file into the container
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application files
COPY app.py .
COPY data.csv .

# 6. Command to execute when container starts
CMD ["python", "app.py"]