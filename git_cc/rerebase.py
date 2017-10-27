"""Rebase from Clearcase starting from master_cc.
   Ususally used after gitcc checkin to avoid duplication of commits: with real data and with changes in ".gitcc".
"""

from .common import *
from . import rebase

def main():
    reset()
    tag(CI_TAG)
    rebase.main()
