#!/usr/bin/env python
""" Tools for creating and retrieving timestamped directories"""
import os
from datetime import datetime

DATETIMEFORMAT = "%Y_%m_%d_%a__%H_%M"

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
    inside of basedir. of a basedir"""
    raise RuntimeError("get_latest_timestamped_dir is not implemented yet.")
