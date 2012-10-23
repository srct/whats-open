#What's Open#

Simple Django site displaying which dining locations are currently open on 
George Mason University's campus.

##Contributing##

What's Open is still in it's very early stages and needs all the help it can
get. Even if you don't feel like you can be helpful with the heavily technical
aspects, we definitely need designers and technical writers.

There are many things that can be done with this project, but sometimes it's the
small things that count, so don't be afraid of contributing just for a spelling
mistake.

If you need help at all please contact me (Tyler). I want people to
contribute, so if you are struggling, or just want to learn, then I am willing
to help.

###Set Up###

To get started, you'll need the following installed:
* [Python 2.7](http://www.python.org/download/)
* [Django 1.4 or later](https://www.djangoproject.com/download/)
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html#installation) 
  (to install you will need either 
  [pip](http://www.pip-installer.org/en/latest/installing.html) or 
  easyinstall, which is bundled with 
  [setuptools](http://pypi.python.org/pypi/setuptools)

Then type the following commands in your terminal (if you're on Windows, 
[Cygwin](http://www.cygwin.com/) is recommended).

```bash
git clone git@git.gmu.edu:whats-open/whats-open.git
cd whats-open/
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate website
```

The git.gmu.edu repository should be available to all SRCT members registered
on the site. If you're not, but would like to contribute, contact me or another
SRCT member.

###Testing the Site Locally###

Now that everything is set-up you can run the server on your computer.

```bash
python manage.py runserver --settings=whats_open.local_settings
```

Go to http://127.0.0.1/ in your browser and you should see the website. 
Though, there won't be any restaurants showing. You will need to add them to 
the database. Go to http://127.0.0.1/admin/ to add new Restaurant and Schedule 
objects to your database.

###Modifying and Deploying Code###

With the means of testing the website, you can really start contributing.

If you're new to Django and don't know where to start, I highly recommend
giving the [tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
a try. However, it leaves out a lot of important things, so remember, Google is
your friend. If you can't figure it out there, ask me.

If you followed the steps in "Set Up" above, once you actually make changes it
should be easy to push them to the git repository.

There are many ways to use git, and this is one example:

```
git commit -a
git push origin master
```

Some more helpful links on how to use Git:
* [Git Reference](http://gitref.org/)
* [OpenHatch's Training Mission](https://openhatch.org/missions/git)
* [Visual Git
  Reference](http://marklodato.github.com/visual-git-guide/index-en.html)
* [Git For Ages 4 And
  Up](http://blip.tv/open-source-developers-conference/git-for-ages-4-and-up-4460524)


###Pedantic Technical Details###

Notice that `whats_open.local_settings` was specified as the settings file when
running the site locally. This settings file, located under the `whats_open`
folder as `local_settings.py`, is identical to the `settings.py` except for a
few things that allow you to run the site locally, like using an sqlite
database instead of the PostgresSQL one used for production currently.

However, it is possible to run the site locally using the PostgresSQL database
and normal `settings.py` file. The most sane way of doing this requires that the 
heroku-toolbelt installed and that you have access to the heroku site as a 
contributor, so see me if you desire this.

###To Do###
* Get all restaurants displaying correct open times on the page. AKA. make
  extensive tests.
* Add a Typeahead search box at the top to quickly filter out restaurants.
* Sort by location view
* Get a decent UI
* Add times until opening/closing for restaurants that are close, and exact
  times for those that aren't.
* Add yellow close-to-closing condition.
* Possible: Make page refresh, or more preferably have the data refresh. For
  example, with AJAX calls.
