############################################################
# Dockerfile to build What's Open Django App
############################################################

# Set the base image to Ubuntu
FROM python:3.6
ENV PYTHONUNBUFFERED 1

# Update the sources list
RUN apt-get update
RUN apt-get install netcat libgdal1h libproj-dev proj-data proj-bin -y

RUN mkdir /whats_open
WORKDIR /whats_open
ADD /requirements/ /whats_open/
RUN pip install -r base.txt
ADD . /whats_open/
