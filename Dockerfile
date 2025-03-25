FROM python:3.13.2-alpine3.21

# Set the working directory inside the container
WORKDIR /app

# Create the ComicCrafterAI folder inside the container
# RUN mkdir -p /app/ComicCrafterAI

# Copy the content of the current directory into /app/ComicCrafterAI
COPY . /app

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app (app.py is inside the Model folder)
CMD ["streamlit", "run", "Model/app.py"]
