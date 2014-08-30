############################################################
# Dockerfile to build What's Open Django App
############################################################

# Instructions:
#
# Note: You need to edit the empty string on the line that
#   says "ENV SECRET_KEY" to be a secure random value.
#
# Any initialized data that needs to be imported should be
#   placed in a directory called "fixtures" in the context
#   of the build.
#   (https://docs.djangoproject.com/en/dev/howto/initial-data/)
#
# Build Command: sudo docker build -t whats_open .
# Run Command: sudo docker run -p 8000:80 -i -t -d whats_open
#
# (You'll need to reverse proxy port 8000 via nginx)

# Set the base image to Ubuntu
FROM ubuntu:14:04

# File Author / Maintainer
MAINTAINER Student-Run Computing and Technology - GMU

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Clone down SRCT-Web
RUN git clone https://github.com/srct/whats-open.git whats-open

# Get pip to download and install requirements:
RUN pip install -r /whats-open/requirements.txt

# Set this to a unique, secure value before building
# (http://www.miniwebtool.com/django-secret-key-generator/)
ENV SECRET_KEY ""

# Set the default directory where CMD will execute
WORKDIR /whats-open/whats_open

# Setup database
RUN python manage.py syncdb --noinput
RUN python manage.py migrate website --noinput

# Generate static files in the STATIC_ROOT location
# (https://docs.djangoproject.com/en/dev/howto/static-files/deployment/)
RUN python manage.py collectstatic --noinput

# Add any inital data fixtures
# (https://docs.djangoproject.com/en/dev/howto/initial-data/)
ADD fixtures /whats-open/whats_open/
# Import the loaded fixtures
RUN python manage.py loaddata users schedules

# Expose ports
EXPOSE 80

# Use Gunicorn to server the application
CMD gunicorn whats_open.wsgi:application -b 0.0.0.0:80
