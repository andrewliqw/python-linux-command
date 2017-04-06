"""
Linux commands.
"""

import os
import shutil


def cd(path=None):
    if path:
        os.chdir(path)
    else:
        home_dir = os.environ['HOME']
        os.chdir(home_dir)


def cp(src, dst, *, follow_symlinks=True):
    shutil.copy(src, dst, follow_symlinks=follow_symlinks)


def mv(src, dst, copy_function=shutil.copy2):
    shutil.move(src, dst, copy_function=copy_function)


def pwd():
    return os.getcwd()


def rm(path):
    os.rmdir(path)


def uname():
    return os.uname()
