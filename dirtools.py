#!/usr/bin/env python
""" Tools for creating and retrieving timestamped directories"""
import os
import re
from datetime import datetime

DATETIMEFORMAT = "%Y_%m_%d_%a__%H_%M"
DATETIME_RE = re.compile("\d{4}_\d{2}_\d{2}_\w{3}__\d{2}_\d{2}")

def ensure_path_exists(pathname):
    """Create the path with name pathName if it doesn't already exist.
    No error checking is performed."""
    if not os.path.exists(pathname):
        os.makedirs(pathname)

def create_timestamped_dir(basedir, datetime_str=None):
    """Create a directory whose name contains date and time inside basedir.
    Returns the name of this directory."""
    if datetime_str is None:
        datetime_str = datetime.now().strftime(DATETIMEFORMAT)
    newdir = os.path.join(basedir, datetime_str)
    ensure_path_exists(newdir)
    return newdir

def get_latest_timestamped_dir(basedir, nth_latest=0):
    """Returns the pathname of the nth_latest timestamped directory
    inside of basedir. Raises Exception if basedir doesn't exist or no
    subdir matching the timestamp is found."""
    timestamped_dirs = [f for f in os.listdir(basedir)
                        if os.path.isdir(os.path.join(basedir, f)) and \
                            DATETIME_RE.match(f)]
    if timestamped_dirs.empty():
        raise RuntimeError("No timestamped dir inside %s" % basedir)
    if nth_latest > len(timestamped_dirs)-1:
        raise RuntimeError("%s only has %d entries, you asked for the %d-th." \
                               % (basedir,len(timestamped_dirs),nth_latest+1))
    return sorted(timestamped_dirs, reverse=True)[nth_latest]
