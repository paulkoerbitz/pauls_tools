#!/usr/bin/env python
"""Convenience Tools for creating loggers"""
import logging
import os
import dirtools

def create_logger(fname):
    """Create a standard logger"""
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.INFO) 
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler = logging.FileHandler(filename=fname)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def create_logfilename(basedir, program_name, logfile_name=None):
    """Create a logfile name of the form 
    basedir/program_name/datetime_stamp/logfile_name"""
    logfile_path = dirtools.create_timestamped_dir(
        os.path.join(basedir,program_name))
    if logfile_name is None:
        logfile_name = "_".join([program_name, "log.txt"])
    return os.path.join(logfile_path, logfile_name)
