# Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy frontend source code to container
COPY . .

# Expose the port on which the application will run
EXPOSE 8501

# Command to run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]