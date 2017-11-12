"""
Exposes a run function that lists all of the files in the current directory and returns tht list as a string. Each
module that you develope should expose a run fucntion that takes a variable number of arguments. This enables you to
load each module the same way and leaves enough extensibility so that you can customize the config files to pass
arguments to the module if you desire.
"""

import os

def run(**args):

    print "[*] In dirlister module."
    files = os.listdir(".")

    return str(files)