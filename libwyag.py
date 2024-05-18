import argparse
import collections
import configparser
import grp, pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

arg_parser = argparse.ArgumentParser(description="dumb tracker")
arg_subparser = arg_parser.add_subparsers(title="Commands", dest="command")
arg_subparser.required = True


def cmd_add(args):
    pass


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    args = arg_parser.parse_args(argv)
    match args.command:
        case "add":
            cmd_add(args)
        case _:
            print("Incorrect Command")
