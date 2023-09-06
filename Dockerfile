# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /what_contact
WORKDIR /what_contact

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     libx11-6 \
#     libxcomposite1 \
#     libxi6 \
#     libxext6 \
#     libxrender1 \
#     libglib2.0-0 \
#     libnss3 \
#     libnspr4 \
#     libasound2 \
#     libxss1

# # Install Chrome
# RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#     && apt install -y ./google-chrome-stable_current_amd64.deb \
#     && rm google-chrome-stable_current_amd64.deb

# # Install ChromeDriver
# RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
#     && wget -q https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
#     && unzip chromedriver_linux64.zip \
#     && mv chromedriver /usr/bin/chromedriver \
#     && chmod +x /usr/bin/chromedriver \
#     && rm chromedriver_linux64.zip

# Copy the current directory contents into the container at /what_contact
COPY . /what_contact

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python", "main.py"]