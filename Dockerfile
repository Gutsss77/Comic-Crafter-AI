FROM python:3.10

# Install system dependencies (e.g., for building PyTorch)
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    libopenblas-dev \
    libomp-dev \
    python3-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce image size

# Set the working directory inside the container
WORKDIR /app

# Copy the content of the current directory into /app
COPY . /app

# List files in /app to check if requirements.txt is copied
RUN ls /app

# Install the Python dependencies from requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install --no-cache-dir torch==1.11.0 -f https://download.pytorch.org/whl/cpu/torch_stable.html
RUN pip install --no-cache-dir torchvision==0.12.0
# RUN pip install --no-cache-dir /path/to/torch.whl
RUN pip install --no-cache-dir --use-deprecated=legacy-resolver -r /app/requirements.txt


# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app (app.py is inside the Model folder)
CMD ["streamlit", "run", "Model/app.py"]


# Build the Docker image
# docker build -t comiccrafterai .

# Run the Docker container
# docker run --name comic_container -p 8501:8501 -v ${pwd}:/app comiccrafterai