"""
Linux commands.
"""

import os
import shutil


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
