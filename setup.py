from setuptools import setup
from m2r import parse_from_file
import restructuredtext_lint
from mister_bump import bump

# Parser README.md into reStructuredText format
rst_readme = parse_from_file('README.md')

# Validate the README, checking for errors
errors = restructuredtext_lint.lint(rst_readme)

# Raise an exception for any errors found
if errors:
    print(rst_readme)
    raise ValueError('README.md contains errors: ',
                     ', '.join([e.message for e in errors]))

setup(
    name="terminal-velocity-git",
    version=bump(),
    author="Sean Hammond, Vincent Perricone, Jon Grace-Cox",
    packages=["terminal_velocity"],
    url="https://github.com/jongracecox/terminal_velocity",
    license="GNU General Public License, Version 3",
    description="A fast note-taking app for the UNIX terminal, with Git support.",
    long_description=rst_readme,
    setup_requires=['setuptools', 'wheel'],
    install_requires=[
        "urwid>=1.1.1",
        "chardet>=2.1.1",
        "sh>=1.12.14",
        "PyYAML>=3.1.2"
        ],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2 :: Only',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        ],
    options={
        'bdist_wheel': {'universal': True}
    },
    entry_points={
        'console_scripts': ['terminal_velocity=terminal_velocity:main',
                            'terminal-velocity=terminal_velocity:main'],
    }

)
