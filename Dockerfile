############################################################
# What's Open API v2
############################################################

# Set the base image to Ubuntu
FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Update the sources list
RUN apt-get update
RUN apt-get install netcat libgdal1h libproj-dev proj-data proj-bin -y

# Copy over all project files into /whats_open
RUN mkdir /whats-open/
WORKDIR /whats-open/
ADD . /whats-open/

# Pip install all required dependecies
RUN pip install -r /whats-open/requirements/base.txt
