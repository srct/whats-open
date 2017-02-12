# Contributing to What's Open

We would love for you to contribute to What's Open and help make it even better 
than it is today! As a contributor, here are the guidelines we would like you to
follow:

 - [Code of Conduct](#coc)
 - [Question or Problem?](#question)
 - [Issues and Bugs](#issue)
 - [Feature Requests](#feature)
 - [Submission Guidelines](#submit)
 - [Coding Rules](#rules)
 - [Commit Message Guidelines](#commit)

## <a name="coc"></a> Code of Conduct

Help us keep What's Open open and inclusive. Please read and follow the 
[GMU Student Code of Conduct][coc].

## <a name="question"></a> Got a Question or Problem?

Please, do not open issues for the general support questions as we want to keep 
GitLab issues for bug reports and feature requests. You've got much better 
chances of getting your question answered on [Slack Group][slack] where 
questions should be asked in their respective channels.

## <a name="issue"></a> Found a Bug?

If you find a bug in the source code, you can help us by
[submitting an issue](#submit-issue) to our [GitLab Repository][gitlab]. Even 
better, you can [submit a Merge Request](#submit-pr) with a fix.

## <a name="feature"></a> Missing a Feature?

You can *request* a new feature by [submitting an issue](#submit-issue) to our 
GitLab Repository. If you would like to *implement* a new feature, please ensure
an issue already exists to be associated with your commits.

* For any **contribution**, first [open an issue](#submit-issue) and outline your proposal so that it can be
discussed. This will also allow us to better coordinate our efforts, prevent duplication of work,
and help you to craft the change so that it is successfully accepted into the project.

## <a name="submit"></a> Submission Guidelines

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search through open issues, maybe an issue for 
your problem already exists and the discussion might inform you of workarounds 
readily available.

We want to fix all the issues as soon as possible, but before fixing a bug we 
need to reproduce and confirm it. In order to reproduce bugs we may 
ask you to describe a use-case that fails to assist in the debugging process. 

In GitLab there are issue templates that you can use which paste in a sample 
format for you to use.

Check out the following issue for an example: [https://git.gmu.edu/srct/whats-open/issues/31](https://git.gmu.edu/srct/whats-open/issues/31)

You can file new issues by filling out our [new issue form][new-issue].

### <a name="submit-pr"></a> Steps to contribute and submit a Merge Request (MR)

Before you submit your Merge Request (MR) consider the following steps:

* Search [GitLab][merge-request] for an open or closed MR that relates to your 
    submission. You don't want to duplicate effort.

* Pull the latest commits from GitLab

    ```sh
    git pull
    ```

* Check into the current development branch:

    All new commits are merged into this development branch before going live on
    the site in a tagged release (merge into master branch). 
    
    ```sh
    git checkout consolidation
    ```

* Create a new git branch:

    ```sh
    git checkout -B ##-shortdescription
    # Example 
    git checkout -B 31-contibution-guidelines-proposal
    ```

    All branches need to follow the above convention (`##-shortdescription`) `##` 
    in this case represents the issue number that your branch is related to. Each
    issue has one and only one branch and each branch has one and only one purpose:
    to add, modify, or remove a feature/bug from the repo. `shortdescription` is 
    a few hyphon (`-`) seperated words that consisely describe the branch. This helps people 
    who may be unfamiliar with the issue number to know at a glance what the branch

* Now you're ready to write your code in your new branch! Make sure to follow
    listed [style](#rules) & [commit](#commit) guidelines/rules when contributing 
    code.

* Unit tests are run at the CI (GitLab-CI) level once you push your code to GitLab.
    We do this to ensure that the project builds properly and passes tests. In general,
    if you are adding some new piece of code like a function you must **include 
    appropriate test cases**. 
    
    For example if I compose the following function:

    ```python
    # file.py
    def oneplus(num):
        return num + 1
    ```

    then I would additionally write the following test case:
    
    ```python 
    # test_file.py
    def TestOneplus(TestCase):
        assertEquals(oneplus(1), 2)    
    ``` 
* Before you push your code to GitLab it is suggested that you run all unit tests locally.
    
    ```sh
    python manage.py test
    ```

* Commit your changes using a descriptive commit message that follows our
    [commit message conventions](#commit). Adherence to these conventions is strongly
    suggested as it makes it easier to determine what each commit does when, for example,
    things break.

     ```sh
     git add --all
     git commit # first line is title, two newlines is description
     ```

* You will need to ask in the slack channel to be added to the GitLab repo. This
    step is necessary such that you have the necessary permissions to push up your
    branch.

* Push your branch to GitLab:

    ```sh
    git push origin ##-shortdescription
    # ex.
    git push origin 31-contibution-guidelines-proposal
    ```

* In GitLab, send a merge request to the current development branch.

* If we suggest changes to your branch then:
  * Make the required updates.
  * Re-run the unit tests to ensure tests are still passing.
  * Rebase your branch and force push to your GitLab repository (this will update
    your Merge Request):

    ```sh
    git rebase consolidation -i
    git push -f
    ```

That's it! Thank you for your contribution! :tada:

#### After your merge request is merged

After your merge request is merged, you can safely delete your branch and merge 
the changes from the main (upstream) repository:

* Delete the remote branch on GitLab either through the GitLab web UI or your 
    local shell as follows:

    ```sh
    git push origin --delete ##-shortdescription
    # ex.
    git push origin --delete 31-contibution-guidelines-proposal
    ```

* Check out the current development branch:

    ```sh
    git checkout consolidation -f
    ```

* Delete the local branch:

    ```sh
    git branch -D ##-shortdescription
    # ex. 
    git branch -D 31-contibution-guidelines-proposal
    ```

* Update your current development branch with the latest upstream version:

    ```sh
    git l --ff upstream consolidation
    ```

## <a name="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you
are working:

* All features or bug fixes **must be tested** by one or more specs (unit-tests).
* We follow [the PEP8 styleguide][style-guide].

## <a name="commit"></a> Commit Message Guidelines

Consistant commit messages are easier to follow when looking through the **project
history**.

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**.  The 
header has a special format that includes a **type** and a **subject**. The **header**
is mandatory.

Layout:

```
<type>: <subject> # this is the <header>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

Sample headers: 

```
docs: update change log to beta.5
```
```
fix: need to depend on latest rxjs and zone.js
```

### \<header> Type
Must be one of the following:

* **build**: Changes that affect the build system or external dependencies 
(example scopes: gulp, broccoli, npm)
* **ci**: Changes to our gitlab-ci configuration files and scripts 
* **docs**: Documentation only changes
* **feat**: A new feature
* **fix**: A bug fix
* **perf**: A code change that improves performance
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **style**: Changes that do not affect the meaning of the code (white-space, formatting,
 etc.)
* **test**: Adding missing tests or correcting existing tests

### \<header> Subject

The subject contains succinct description of the change.

Sample Subject:

```
add in contributing guide
```

### Body

The body should include a brief description of the changes made in the commit to
provide additional detail.

Sample Body:

```
- Introduce my proposal for CONTRIBUTING.md
- Filled with the whats-open-web contributing guide but contains friendlier language
```

### Footer

The footer should contain any information about **Breaking Changes** (**Breaking 
Changes** should start with the word `BREAKING CHANGE:` with a space or two newlines.
The rest of the commit message is then used for this. and is also the place to 
reference GitLab issues that this commit **Closes**.

Sample footers:
```
BREAKING CHANGE: remove outdated dependency from requirements.txt. be sure to 
reinstall your packages in order for the project to build.
```

```
Closes #31
```
This "Closes" statement should only be incuded in commits that resolve an issue.
What's nice about the statement itself is that when the commit is merged, the issue
will auto close.

[coc]: https://studentconduct.gmu.edu/wp-content/uploads/2011/09/2016-17-Code-of-Student-Conduct.pdf
[gitlab]: https://git.gmu.edu/srct/whats-open
[style-guide]: https://www.python.org/dev/peps/pep-0008/
[slack]:https://srct.slack.com/
[new-issue]:https://git.gmu.edu/srct/whats-open/issues/new
[merge-request]:https://git.gmu.edu/srct/whats-open/merge_requests