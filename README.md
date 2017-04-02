# What's Open

[![build status](https://git.gmu.edu/srct/whats-open/badges/master/build.svg)](https://git.gmu.edu/srct/whats-open/commits/master) [![coverage report](https://git.gmu.edu/srct/whats-open/badges/master/coverage.svg)](https://git.gmu.edu/srct/whats-open/commits/master) [![python version](https://img.shields.io/badge/python-2.7-blue.svg)]() [![Django version](https://img.shields.io/badge/Django-1.10-brightgreen.svg)]()

The What's Open project is an initiative at George Mason University by Mason
Student Run Computing and Technology (SRCT) to display which dining locations
are currently open on George Mason University's campus.

This repo is a simple Django Rest Framework (DRF) project that contains the
database backend and API for SRCT developed What's Open applications. 

What's Open needs all the help it can get. Even if you don't feel 
like you can be helpful with the heavily technical aspects, 
we definitely need designers and technical writers.
 
There are many things that can be done with this project (see the project [Issues](https://git.gmu.edu/srct/whats-open/issues) 
section), but sometimes it's the small things that count, so don't be afraid of 
contributing just for a spelling mistake.

If you need help at all please contact any SRCT member in the `#whats-open` 
channel in our [slack group](https://srct.slack.com). We want people to 
contribute, so if you are struggling, or just want to learn, then we are 
willing to help.

Check out some of the other What's Open projects!
 - [https://git.gmu.edu/srct/whats-open-android]()
 - [https://git.gmu.edu/srct/whats-open-ios]()
 - [https://git.gmu.edu/srct/whats-open-web]()
 - [https://git.gmu.edu/srct/whats-open-alexa]()

# Setup instructions for local development

What's Open currently supports developers on Linux and macOS systems. Here's our 
walk-through of steps we will take:

1. Install `git` on your system.
2. Clone the whats-open codebase.
3. Get whats-open up and running with the method of your choice.

## 1) Install `git` on your system.

`git` is the version control system used for SRCT projects.

### On Linux Based Systems

**with apt:**

Open a terminal and run the following command:

    sudo apt update

This retrieves links to the most up-to-date and secure versions of your packages.

Next, with:

    sudo apt install git

you install `git` onto your system.

**with pacman:**
  
    pacman -S git

### On macOS

We recommend that you use the third party Homebrew package manager for macOS,
which allows you to install packages from your terminal just as easily as you
could on a Linux based system. You could use another package manager (or not
use one at all), but Homebrew is highly reccomended.

To get homebrew, run the following command in a terminal:

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)

**Note**: You do NOT need to use `sudo` when running any Homebrew commands, and
it likely won't work if you do.

Next, to make sure Homebrew is up to date, run:

    brew update

Finally we can install git with:

    brew install git

## 2) Clone the whats-open codebase

Now, we're going to clone down a copy of the whats-open codebase from [git.gmu.edu](http://git.gmu.edu/srct/whats-open),
the SRCT code respository with SSH.

**a)** Configure your ssh keys by following the directions at:

[git.gmu.edu/help/ssh/README](http://git.gmu.edu/help/ssh/README).

**b)** Now, on your computer, navigate to the directory in which you want to download the project (ie. perhaps one called `development/SRCT`), and run

    git clone git@git.gmu.edu:srct/whats-open.git

## 3) Get whats-open up and running

Now that we have `git` setup and cloned down the code you can

    cd whats-open/

and get to working on setting up a development environment! There are two options
to go about doing this: `Docker` and `Manual Setup`.

### Docker

We can automate the setup process through [Docker](https://www.docker.com/what-docker)
containers! This allows us to quickly get started and standardize development
environments across machines.

Installing Docker on your system:

 - For macOS: [https://docs.docker.com/docker-for-mac/]()
 - For Windows: [https://docs.docker.com/docker-for-windows/]()
 - For your specific *nix distro: [https://docs.docker.com/engine/installation/]() 

Additionally, you will need to install docker-compose: [https://docs.docker.com/compose/install/]()

Next inside the `whats-open/` root directory run:

    docker-compose build

If that doesn't work, try:

    sudo docker-compose build

Then, follow up with:

    docker-compose up

If that doesn't work, try:

    sudo docker-compose build

You should see that the server is running by going to [http://localhost:8000]()
in your browser. Any changes you make to your local file system will be mirrored in the server.

If you would like to log into the admin interface then use the following credentials:

```
user: admin@masonlive.gmu.edu
pass: admin
```

### Manual Setup

Manual Setup involves all of the same steps as Docker, but just done manually.

First, install python, pip, and virtualenv on your system.
  * `python` is the programming language used for Django, the web framework used by whats-open.
  * `pip` is the python package manager.
  * `virtualenv` allows you to isolate pip packages within virtual environments

Open a terminal and run the following command:

    sudo apt update

Next, with:

    sudo apt install python3 python3-dev python3-pip 
    sudo pip3 install virtualenv

you install `python`, `pip`, and `virtualenv`.

#### Database Setup

What's Open is built on top of a `MySQL` database and thus, we must set it up.

Run:

    sudo apt install mysql-server mysql-client libmysqlclient-dev python-mysqldb

to install mysql packages onto your system.

Load up the mysql shell by running

    mysql -u root -p

and putting in your mysql password.

Create the database by running:

    CREATE DATABASE wopen;

You can choose a different name for your database if you desire.

Double check your database was created by running:

    SHOW DATABASES;

Though you can use an existing user to access this database, here's how to create
a new user and give them the necessary permissions to your newly created database:

    CREATE USER 'wopen'@'localhost' IDENTIFIED BY 'password';

For local development, password strength is less important, but use a strong 
passphrase for deployment. You can choose a different username.

    GRANT ALL ON wopen.* TO 'wopen'@'localhost';

This allows your database user to create all the tables it needs on the What's 
Open database.

Run:

    GRANT ALL ON test_wopen.* TO 'wopen'@'localhost'; FLUSH PRIVILEGES;

When running test cases, django creates a test database so your 'real' database
doesn't get screwed up. This database is called 'test_' + whatever your normal 
database is named. Note that for permissions it doesn't matter that this database 
hasn't yet been created.

The .* is to grant access all tables in the database, and 'flush privileges' 
reloads privileges to ensure that your user is ready to go.

Exit the mysql shell by typing:

    exit


At this point we will need to set some environment variables. 

If you are using bash then just copy paste the following into your terminal:

```
export WOPEN_SECRET_KEY=$(dd if=/dev/urandom count=100 | tr -dc "A-Za-z0-9" | fold -w 60 | head -n1 2>/dev/null)
export WOPEN_EMAIL_DOMAIN="@masonlive.gmu.edu"
export WOPEN_DB_NAME="wopen"
export WOPEN_DB_USER="wopen"
export WOPEN_DB_PASSWORD="password"
export WOPEN_DB_PORT=3306
export WOPEN_DB_HOST=
```

## The Virtual Enviornment

Virtual environments are used to keep separate project packages from the main 
computer, so you can use different versions of packages across different 
projects and ease deployment server setup.

It's often recommended to create a special directory to store all of your 
virtual environments together (ie. development/virtualenv/), though they can be 
placed wherever is most convenient.

Then in your virtual environment directory run:

    virtualenv -p python3 whats_open
    source whats_open/bin/activate

to create your virtual environment and activate it. If you ever need to exit 
your virtual environment, simply run:

    deactivate

Now, the packages you need to install for Go are in in the top level of the 
project's directory structure(whats-open/).

Next with,

    pip install -r requirements.txt
    cd whats_open/
    python3 manage.py makemigrations
    python3 manage.py migrate

you setup the project.

# Running the local web server

Now that everything is set-up you can run the server on your computer.

    python3 manage.py runserver

Go to [http://127.0.0.1:8000/]() in your browser and you should see the website. 

Initially, there won't be any restaurants showing. You will need to add them to 
the database. 

Run,

    python manage.py createsuperuser

to create a superuser to use when signing in to the admin interface. 

Go to [http://127.0.0.1:8000/admin/]() to add new Restaurant and Schedule objects 
to your database.

With that, everything should be good to go!

# Modifying and Deploying Code

With the means of testing the website, you can really start contributing.

If you're new to Django and don't know where to start, I highly recommend
giving the [tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
a try. However, it leaves out a lot of important things, so remember, Google is
your friend.
For the JavaScript, I will be using jQuery whenever possible because I prefer
it to straight up JavaScript. jQuery has [great
documentation](http://docs.jquery.com/) and I've found [Mozilla's documentation
on JavaScript](https://developer.mozilla.org/en-US/docs/JavaScript) to be
useful as well. But if your Google-fu is sharp, that should suffice.

## CONTRIBUTING.md

This document goes into detail about how to contribute to the repo, including 
guidelines for commit messages and details on the workflow of the project.

## Opening issues

There are templates for issue descriptions located on the new issue page. I will
close issues with poor descriptions or who do not follow the standard.

## Coding style

You should adhere to the style of the repo code. Consistancy is key! PEP8 
guidelines are strongly reccomended but not enforced at the time. Please comment your code, I will not accept commits that contain uncommented code.

## Getting Help

I encourage you to join the [#whats-open channel](https://srct.slack.com/messages/go/details/) in SRCT's [Slack Group](https://srct.slack.com)
if you have any questions on setup or would like to contribute.
