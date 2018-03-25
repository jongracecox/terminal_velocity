"""
Git helper module for terminal velocity.
"""
from __future__ import print_function
import os
import logging
import yaml
import sh
import getpass
import socket


GIT_CONFIG_FILE = '~/.git_notes_project.yaml'
DEFAULT_LOCAL_PROJECT_DIRECTORY = '~/Notes'

logger = logging.getLogger("terminal_velocity")


def get_git_project_config():
    """Return Git project config."""
    full_config_path = os.path.abspath(os.path.expanduser(GIT_CONFIG_FILE))
    logger.debug('Git project config: %s', full_config_path)

    if not os.path.exists(full_config_path):
        logger.warning('Config file does not exist: %s', full_config_path)
        return None

    with open(full_config_path, 'r') as file_handle:
        try:
            config = yaml.load(file_handle)
            return config
        except yaml.YAMLError as exc:
            logger.error('Failed to parse config file: %s', exc)
            return None


def git_project_is_configured():
    """Return True if project is configured."""
    if get_project_url():
        return True
    return False


def get_project_url():
    """Returns project URL from user."""
    config = get_git_project_config()

    if not config:
        return None

    if 'project url' in config:
        return config['project url']

    return None


def get_local_project_directory():
    """Return the local project directory."""
    config = get_git_project_config()

    if not config:
        return os.path.expanduser(DEFAULT_LOCAL_PROJECT_DIRECTORY)
    if 'project directory' in config:
        return os.path.expanduser(config['project directory'])
    return os.path.expanduser(DEFAULT_LOCAL_PROJECT_DIRECTORY)


def is_git_project_directory(directory):
    """Return True if directory is a Git project directory."""
    return os.path.exists(os.path.expanduser(directory) + '/.git')


def init_project():
    """Initialise a local copy of a Git project."""
    git = sh.Command('git')
    git('init', _cwd=get_local_project_directory())
    git('remote', 'add', 'origin', get_project_url(), _cwd=get_local_project_directory())


def fetch_changes():
    """Fetch changes from Git project."""
    if not is_git_project_directory(get_local_project_directory()):
        init_project()

    print('Fetching changes from Git...')
    git = sh.Command('git')

    try:
        git('pull', 'origin', 'master', _cwd=get_local_project_directory())
    except sh.ErrorReturnCode_128 as e:
        print('Failed to refresh local project directory: %s' % e.stderr)
        raw_input('Press ENTER to continue...')


def project_directory_changed():
    """Return True if project directory changed."""
    git = sh.Command('git')
    changes = git('diff-index', '--name-only', 'HEAD', '--', _cwd=get_local_project_directory())
    if len(changes):
        return True
    return False


def push_changes(commit_message=None):
    """Push changes to a Git project."""
    if not project_directory_changed():
        print('No Git project changes.')
        return

    if not commit_message:
        username = getpass.getuser()
        hostname = socket.gethostname()
        commit_message = 'Updated by %s on %s' % (username, hostname)

    print('Pushing changes to Git...')
    git = sh.Command('git')
    try:
        git('add', '-A', _cwd=get_local_project_directory())
        git('commit', '-m', commit_message, _cwd=get_local_project_directory())
        git('push', _cwd=get_local_project_directory())
    except sh.ErrorReturnCode_128 as e:
        print('Failed to push local project changes: %s' % e.stderr)
        raw_input('Press ENTER to continue...')
