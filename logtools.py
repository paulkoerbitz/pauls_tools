#!/usr/bin/env python

"""Convenience Tools for creating loggers"""
import logging
import os
from datetime import datetime

def createLogger(fname):
    """Create a standard logger"""
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.INFO) 
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    handler = logging.FileHandler(filename=fname)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def createLogFilename(basedir,programName,logfileName=None,dateTimeStr=None):
    """Create a logfile name of the form 
    basedir/programName/DateTimeStamp/logfileName"""
    if dateTimeStr is None:
        dateTimeStr = datetime.now().strftime("%Y-%m-%d-%a--%H-%M")
    logfilePath = os.path.join(basedir,programName,dateTimeStr)
    ensurePathExists(logfilePath)
    if logfileName is None:
        logfileName = "-".join([programName,"log.txt"])
    return os.path.join([logfilePath,logfileName])

def ensurePathExists(pathName):
    """Create the path with name pathName if it doesn't already exist."""
    d = os.path.dirname(pathName)
    if not os.path.exists(d):
        os.makedirs(d)
