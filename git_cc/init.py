"""Initialise gitcc with a clearcase directory"""

from .common import *
from os import open
from os.path import join, exists, abspath

def main(ccdir):
    git_exec(['config', 'core.autocrlf', 'false'])
    cfg.set(CFG_CC, abspath(ccdir))
    cfg.write()
