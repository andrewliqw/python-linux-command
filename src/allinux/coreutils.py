"""
https://www.gnu.org/software/coreutils/manual/html_node/index.html
"""

import os
import shutil

#
# Basic operations
#

def cp(src, dst, *, recursive=False, follow_symlinks=True):
    """
    Mimic 'cp' command.
    
    recursive is True, mimic 'cp -r'.
    """
    if os.path.isdir(src):
        if recursive:
            shutil.copytree(src, dst, symlinks=follow_symlinks)
    else:
        shutil.copy2(src, dst, follow_symlinks=follow_symlinks)


#
# Special file types
#

def mkdir(path, recursive=False, mode=0o777, *, dir_fd=None):
    """
    Mimic 'mkdir' command.
    
    If recursive is True, equal to 'mkdir -p'.
    """

    if recursive:
        os.makedirs(path, mode, exist_ok=True)
    else:
        os.mkdir(path, mode, dir_fd=dir_fd)


def mv(src, dst, copy_function=shutil.copy2):
    shutil.move(src, dst, copy_function=copy_function)


def rm(path):
    os.rmdir(path)


def uname():
    return os.uname()
