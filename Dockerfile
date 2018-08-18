############################################################
# What's Open API v2
############################################################

# Set the base image to Ubuntu
FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Update the sources list and install all packages
# See: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run
RUN apt-get update && apt-get install -y \
    netcat \
    libproj-dev \
    proj-data \
    proj-bin \
    binutils \ 
    gdal-bin \ 
    && rm -rf /var/lib/apt/lists/*

# Copy over all project files into /whats_open
RUN mkdir /whats-open/
WORKDIR /whats-open/
ADD . /whats-open/

# Pip install all required dependecies
RUN pip install -r /whats-open/requirements/base.txt
