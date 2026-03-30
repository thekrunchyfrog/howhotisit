# Build stage
FROM dtcooper/raspberrypi-os:python AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc swig build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && wget http://abyz.me.uk/lg/lg.zip \
    && unzip lg.zip \
    && cd lg \
    && make install \
    && cd .

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM dtcooper/raspberrypi-os:python

WORKDIR /app

# Install runtime dependencies for GPIO/temperature sensor
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgpiod2 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local

# Ensure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY app.py .
COPY sensor.py .
COPY temperaturedb.py .

# Create volume for database
VOLUME /app/data

# Expose port
EXPOSE 8080

# Run the Flask app
CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0", "--port=8080"]
