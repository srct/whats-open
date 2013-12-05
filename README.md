What's Open
===

Simple Django site displaying which dining locations are currently open on 
George Mason University's campus.

Contributing
---

What's Open is still in its very early stages and needs all the help it can
get. Even if you don't feel like you can be helpful with the heavily technical
aspects, we definitely need designers and technical writers.

There are many things that can be done with this project (see the "To Do" 
section), but sometimes it's the small things that count, so don't be afraid of 
contributing just for a spelling mistake.

If you need help at all please contact any SRCT member. We want people to
contribute, so if you are struggling, or just want to learn, then we are willing
to help.

Set Up
---

To get started, you'll need the following installed:

* [Python 2.7](http://www.python.org/download/)
* [Django 1.4 or later](https://www.djangoproject.com/download/)
* [Git](http://git-scm.com/book/en/Getting-Started-Installing-Git)
* [virtualenv](http://www.virtualenv.org/en/latest/index.html#installation) 
  (to install you will need either 
  [pip](http://www.pip-installer.org/en/latest/installing.html) or
  [easy_install](http://pythonhosted.org/distribute/easy_install.html))

<!--You don't need to do anything with [git.gmu.edu](https://git.gmu.edu/) to -->
<!--preform a `git clone`, but you should log in if you plan on actually modifying -->
<!--code. Logging into git.gmu.edu with your George Mason credentials will create -->
<!--an account. Ask a SRCT member to add you to the SRCT group on the site and you -->
<!--will be added to the list of people allowed to `git push` to the repository at -->
<!--git.gmu.edu. Alternatively, you can fork the project, clone your own repo, make -->
<!--changes there, and submit pull requests.-->

Then type the following commands in your terminal (if you're on Windows, 
[Cygwin](http://www.cygwin.com/) is recommended).

```bash
git clone http://git.gmu.edu/srct/whats-open.git
cd whats-open/
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
python manage.py syncdb
python manage.py migrate website
```

Running the Site Locally
---

Now that everything is set-up you can run the server on your computer.

```bash
python manage.py runserver
```

Go to http://127.0.0.1:8000/ in your browser and you should see the website. 
Though, there won't be any restaurants showing. You will need to add them to 
the database. Go to http://127.0.0.1:8000/admin/ to add new Restaurant and Schedule 
objects to your database (the login would be the same username and password you 
entered when creating a superuser during the `python manage.py syncdb` command).

Modifying and Deploying Code
---

With the means of testing the website, you can really start contributing.

If you're new to Django and don't know where to start, I highly recommend
giving the [tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01/)
a try. However, it leaves out a lot of important things, so remember, Google is
your friend. If you can't figure it out there, ask me.

For the JavaScript, I will be using jQuery whenever possible because I prefer
it to straight up JavaScript. jQuery has [great
documentation](http://docs.jquery.com/) and I've found [Mozilla's documentation
on JavaScript](https://developer.mozilla.org/en-US/docs/JavaScript) to be
useful as well. But if your Google-fu is sharp, that should suffice.

<!--If you followed the steps in "Set Up" above, once you actually make changes it-->
<!--should be easy to push them to the git repository.-->

Once you actually make your changes and have fully tested them you can push the 
code to the git repository. The best way to do this is to fork the project, make
the changes in your local repository, push to gitlab, and submit a pull request.

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

We currently don't have What's Open running on a dedicated server yet, but when
we do I will have instructions on how to deploy the code here.

<!--No longer relevant as there is no postgres database set up at the moment-->
<!--###Running Site Locally with Production Database###-->
<!--It is possible to run the site locally using the PostgresSQL database that-->
<!--whatsopen.gmu.edu uses. The way settings.py is configured requires that you set-->
<!--an environmental variable to the database's url before you run the site. Talk -->
<!--to me if you would like to know the url to accomplish this.-->

To Do
---

* Get all restaurants displaying correct open times on the page. AKA. make
  extensive tests.
* Sort by location view
* Add times until opening/closing for restaurants that are close, and exact
  times for those that aren't.
* Make page refresh, or more preferably have the data refresh. For
  example, with AJAX calls.
* Create more useful API calls. Document them.
* Allow switching between campuses. In the database, mark which campus each
  restauraunt is on, include this information in the JSON object returned at
  `ajax/schedule` and store the campus choice in the user's cookies
  so that when they come back the page will already be set to their campus.
  Default would be Fairfax of course.
  [jquery-cookie](https://github.com/carhartl/jquery-cookie) would be useful
  for this.
