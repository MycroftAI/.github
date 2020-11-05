# Contributing to Mycroft AI

:tada: First, thanks for supporting the development of open source voice technologies! :tada:

This is a general guide for how to contribute to Mycroft's repositories. That includes anything hosted in the [MycroftAI Organisation](https://github.com/MycroftAI) on Github. These are mostly guidelines, not rules. Following them should make it easier to get your contribution reviewed, merged and deployed more quickly. However we encourage you to use your best judgment, and feel free to propose changes to this document in a pull request.

## Code of Conduct
This project and everyone participating in it is governed by the [Mycroft Contributor Covenant Code of Conduct](https://github.com/MycroftAI/.github/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to support@mycroft.ai.

## I just have a question

If you have a question about Mycroft or one of our technologies, please head to the [Community Forums](https://community.mycroft.ai/).

If you prefer to chat, there is also [Mycroft Chat](https://chat.mycroft.ai/) powered by Mattermost. Please note that whilst this is a live chat service, responses may come immediately or may take a number of hours. This all depends on who in the Community is available. Deep work is important to all developers so please be patient.

When asking a question, help us to help you. Please provide as much detail as possible. We have a quick [guide for what is useful to include](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/troubleshooting/getting-more-support).

## What can I contribute to?

If you are looking for a way to contribute to Mycroft there are so many ways to get involved. This includes coding, design, translation, testing, and much more. Take a look at our website to see what you can do: http://mycroft.ai/contribute

Looking for a bug to fix, or a feature to implement? Check out the [Github items labelled `help wanted`](https://github.com/issues?q=is%3Aopen+is%3Aissue+user%3AMycroftAI+archived%3Afalse+label%3A%22help+wanted%22) for inspiration. If you spot something you want to work on, comment in that thread so others know you're working on it.

## Contributing to a repository

So you are ready to work on one of our Github repositories. Let's get into it!

_Note: These are general guidelines and should work for most Python projects._

### Sign the Contributor Licensing Agreement (CLA)

To protect yourself, the project, and users of Mycroft technologies, we require a Contributor Licensing Agreement (CLA) before accepting any code contribution. This agreement makes it crystal clear that, along with your code, you are offering a license to use it within the confines of this project. You retain ownership of the code, this is just a license.

You will also be added to our [list of excellent humans](https://github.com/MycroftAI/contributors)!

Please visit https://mycroft.ai/cla to initiate this one-time signing.

### Fork and clone the project

Github provide an excellent guide on this already. So if you are new to Git, check this out first:
https://guides.github.com/activities/forking/

### Setup the project

The majority of our technologies are written in Python, and this section presumes you are working on one of these projects. If you are looking at one of our non-Python repositories, please check the README or specific contributing guide for that project.

#### Creating a Python virtual environment
Rather than installing this directly onto your system, we strongly encourage the use of virtual environments. This creates an isolated Python environment allowing you to run everything using a specific version of Python, install different versions of dependencies, and when you're finished - delete everything quickly and easily.

Again, there are many tutorials online for setting up a virtual environment including the Python documentation itself:
https://docs.python.org/3/library/venv.html

Most of the time, the following should work on regular Linux install using a bash shell:
```
cd /path/to/my/project     # Change to our working directory
python3 -m venv .venv      # Create a virtual environment in .venv
source .venv/bin/activate  # Activate our new virtual environment
```

After activating the virtual environment your command prompt will be prepended to show the activated venv. So if your shell usually displays:
```shell
user@computer:~/my-project$
```

With the above venv active it will display:
```shell
(.venv) user@computer:~/my-project$
```

To deactivate the venv run the `deactivate` command.

As mentioned above you can remove this virtual environment by simply deleting the `.venv` directory that we created it in.

#### Running the setup script
Most of our Python projects provide a `setup.py` file that contains the instructions for what's included and how it should be installed. This means that setup requires a single command:

```shell
python setup.py install    # Run the setup script
```

#### Ensure it is working first

Now we have the software package setup. Before making any changes, we recommend running the available tests to be sure everything is working as expected.

The tests available will differ depending on the project, but [running pytest](https://docs.pytest.org/en/stable/getting-started.html) is a good start.

### Making changes

Now that we have all the code working on our local machine, we're ready to make changes.

#### Create or comment on an issue
If one does not already exist, [create a new issue](https://help.github.com/articles/creating-an-issue/) on the relevant repository. 

If you have selected an existing issue to work on, it is a good practice to comment and let others know you are working on it. This prevents duplication of work. 

The issue is also a good place to ask any clarifying questions or to seek help if you get stuck.

#### Create a feature branch
From the default branch of the repository, create a new feature or bugfix branch using the issue number from the repository. For example, if your issue identifier is: issue-123 then you will create either: 
- `feature/issue-123` for issues related to new functionalities or enhancements; or
- `bugfix/issue-123` for issues that relate to bugs in the code.

#### Test Driven Development
We strongly encourage the use of [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development). There are many opinions on the ideal TDD approach but broadly it consists of the following steps:
1. Write a test - clearly define the function or improvements to an existing function.
2. Run all tests - your new test should fail because you haven't written the code yet. 
3. Write the code - fix the bug or implement the feature.
4. Run all tests - your new test should pass because the code is now implemented.
5. Refactor code - now that we know the code is working, we can spend some time cleaning up our code.

#### Code styling
Before committing, format your code following the PEP8 rules. It is also a good practice to organize your imports remove any unused modules. To check whether you are following these rules, you can use tools built into your IDE, or install pycodestyle and run it against a single file or a directory:

```shell
pip install pycodestyle
pycodestyle /path/to/my/project
```

/* #TODO: Add more detail on Mycroft's preferred styling */

#### Documentation

Code should be documented using [Google-style docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). Our automated documentation tools expect that format. 

All functions and class methods that are expected to be called externally should include a docstring. Any function that should not be called externally should be prefixed with a single underscore to indicate that it is a private function.

### Committing code

Committed your code in logical units with each having a clear commit message is helpful for both the reviewers, and anyone looking at your code in the future (including yourself).

#### Commit messages

Good commit messages provide a brief summary of the change and explain why the change was made. Together, they provide an overview of the codes history.

/* #TODO: add a commit message template */

#### Submitting a Pull Request

After pushing your code up to your fork of the project, you can open a [Pull Request](https://help.github.com/articles/using-pull-requests/) back to the upstream project.

Like commit messages, the PR title and description should properly describe the changes you have made, along with any additional information that reviewers and other developers might need.

The pull request should be pre-populated with a template specific to that project. Please read this carefully and provide all the necessary information.

#### Pull request labels

Pull requests submitted to a Mycroft repository may receive the following labels to help both the project and the contributor know the status of the PR.

These are broadly color coded in order to provide a quick indication as to the broad meaning of a label and the actions required:

- Blue (#22a7f0)  = Informative label only.
- Green (#0e8a16)  = On track. Ready for progress by any contributor.
- Yellow (#fbca04)  = Action required. Input from author or other contributor familiar with the PR is likely required.
- Purple (#5319e7)  = Team action required. A member of the Community or internal teams likely needed to progress.
- Orange (#ff9900)  = PR is being intentionally held for some reason.
- Red (#b60205)  = PR closed. No further action will be taken.

| Label name | Description |
| --- | --- |
| Type: Bug - quick | Bug fixes that are quick to review and the implications of the change are clear and contained. Eg typo’s, error handling, etc. |
| Type: Bug - complex | Bug fixes that touch multiple points of the codebase or where the change may have other consequences. Eg: adding new classes, changing Messagebus Types, etc. |
| Type: Enhancement - proposed | New proposal for a feature that is not on the current roadmap. |
| Type: Enhancement - roadmapped | Implementation of a feature that is on the roadmap. |
| Type: Refactoring and other improvements | Improvement of code and documentation that does not alter functionality. |
| Type: Tests | Addition or improvement of automated tests |
| Status: Work in Progress | PR being actively worked on, not yet ready for review. |
| Status: For Discussion | Feature proposal in development. Community input and discussion is invited. |
| Status: For Voting | Feature proposal to be voted on by the Community. |
| Status: To be reviewed | Concept accepted and has sufficient information for code review. |
| Status: In review | Has been assigned for review. |
| Status: Escalated | Requires additional review by experienced member or someone familiar with a specific system. |
| Status: Change requested | Some action is required by the author. Eg: revision of the code, addition of tests or documentation, or further information describing the PR and its purpose. |
| Status: Approved | PR has been reviewed and accepted.  |
| Merge after next release | PR should not be merged until after the next release. |
| Breaking change | PR contains breaking changes and should not be merged until the next major release is being prepared. |
| Status: Not accepted | PR will not be accepted by the project. Clear feedback should be provided as to why it was not accepted and how the author might modify or improve it. |
| Status: Abandoned by author | Author has not responded and PR will be (or has been) closed.  |
| Help wanted | An issue seeking contributors. Should be well defined ready for someone to work on. |
| good first issue | Good issue for new contributors |
| CLA: Yes | Author has signed CLA - see https://github.com/mycroftai/contributors |
| CLA: Needed | Author has not yet signed CLA - please visit https://mycroft.ai/cla |
| hacktoberfest | Special tag for Hacktoberfest |
| invalid | Special tag for Hacktoberfest - indicates spam PR |

### Reviewing PR's

While you wait for a review of your contribution, why not take a moment to review some other pull requests? 

Reading other peoples code is a great way to learn, and helping us process the queue of pull requests means your own contribution will be seen more quickly!

#### Tips for reviewing other peoples code

/* #TODO: Add a guide for reviewing PR's */