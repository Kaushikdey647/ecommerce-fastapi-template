FROM python:3.11.3

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY ./requirements.txt /app/requirements.txt

# Install the required packages
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the rest of the application files to the container
COPY . /app

# Expose the port that the application will run on
EXPOSE 80

# Start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]