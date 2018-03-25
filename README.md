# Terminal Velocity

![build status](https://travis-ci.org/jongracecox/terminal_velocity.svg?branch=master)

Terminal Velocity is a fast note-taking app for the UNIX terminal, that
focuses on letting you create or find a note as quickly and easily as
possible, then uses your `$EDITOR` to open and edit the note. It is
heavily inspired by the OS X app [Notational
Velocity](http://notational.net/). For screenshots and features, see the
[Terminal Velocity website](http://vhp.github.com/terminal_velocity).

This is a fork of the original project, which adds the ability to
automatically pull and push your Notes changes to a Git project.
When you start terminal velocity it will automatically pull from the
configured git project, and when you exit it will automatically push.

## Installation

### pip - Python package manager
To install Terminal Velocity, run:

    pip install terminal-velocity-git

Then to launch it just run one of the following commands:

    terminal_velocity
    terminal-velocity

To use a different notes directory, run:

    terminal_velocity path/to/your/notes/dir

To see all the command-line options, run:

    terminal_velocity -h

To quit the app, press `ctrl-c` or `ctrl-x`.

To upgrade Terminal Velocity to the latest version, run:

    pip install --upgrade terminal_velocity

To uninstall it, run:

    pip uninstall terminal_velocity

### From Source

Ensure python modules `urwid`, `setuptools`  and `chardet` are installed. Python-dev also.

```
apt install python-setuptools python-chardet python-urwid python-dev
```

Clone the repository from:

    git@github.com:vhp/terminal_velocity.git
    or
    https://github.com/vhp/terminal_velocity.git

Move into terminal_velocity directory you just cloned and run the following:

    sudo python setup.py install

## Sync your notes to Git

You will need:

* A GitHub or GitLab project (for free private projects GitLab is recommended)
* The clone URL of the git project

Before setting this up **!!take a backup of your existing Notes directory!!**.

Create file `~/.git_notes_project.yaml`, and add the following:

```yaml
project url: <git-project-url>
```

Optionally you can change the directory that `terminal-velocity` uses for notes
by adding the following to the file:

```yaml
project directory: ~/My-Other-Notes-Directory
```

Note that this configuration does not affect the terminal velocity configuration,
only the Git project management add-on.

When you start `terminal-velocity` it will automatically initialise the Git project
within your Notes directory

## Releasing to PyPi

To release a new version of Terminal Velocity:

1.  Make sure you have setup your \~/.pypirc file for PyPi uploading
2.  Increment the version number in the [setup.py file](setup.py), add
    an entry te the [changelog](CHANGELOG.txt), commit both changes to
    git and push them to github. For example, see
    [aae87b](https://github.com/seanh/terminal_velocity/commit/aae87bcc50f88037b8fc76c78c0da2086c5e89ae).
3.  Upload the new release to [the terminal\_velocity package on
    pypi](https://pypi.python.org/pypi/terminal_velocity): run
    `python setup.py sdist upload -r pypi`.

For more information see <https://packaging.python.org/>.

## Other things
To make a bug report or feature request, use [GitHub
Issues](https://github.com/vhp/terminal_velocity/issues).

To contribute documentation, use [the
wiki](https://github.com/vhp/terminal_velocity/wiki).

To contribute code to Terminal Velocity, see
[CONTRIBUTING](https://github.com/vhp/terminal_velocity/blob/master/CONTRIBUTING.md#contributing-to-terminal-velocity).

