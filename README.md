#What's Open#

Simple Django site displaying which dining locations are currently open on George Mason University's campus.

##Contributing##

To get started, you'll need the following installed:
* [Python 2.7](http://www.python.org/download/)
* [Django 1.4 or later](https://www.djangoproject.com/download/)
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html#installation) (to install you will need either [pip](http://www.pip-installer.org/en/latest/installing.html) or easy_install, which is bundled with [setuptools](http://pypi.python.org/pypi/setuptools)

Then type the following commands in your terminal (if you're on Windows, [Cygwin](http://www.cygwin.com/) is recommended).

```bash
git clone git@github.com:thallada/whats-open.git
cd whats-open/
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py schemamigration website --auto
```

Now that everything is set-up you can run the server on your computer.

```bash
python manage.py runserver
```

Go to http://127.0.0.1/ in your browser and you should see the website. Though, there won't be any restaurants showing. You will need to add them to the database. Go to http://127.0.0.1/admin/ to add new Restaurant and Schedule objects to your database.
