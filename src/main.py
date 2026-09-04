import re
import os
import sys
import subprocess
import shutil

from pathlib import Path
from platformdirs import user_config_path


def strip_app_name(file_name):
    if bool(re.search("-", file_name)):
        return re.split(r"-[0-9]", file_name)[0]
    elif bool(re.search("_", file_name)):
        return re.split(r"_[0-9]", file_name)[0]
    else:
        return file_name


def executable_permission(pathfile):
    try:
        subprocess.run(["test", "-x", pathfile], check=True)
    except subprocess.CalledProcessError:
        if os.geteuid() != 0:
            print("Run using sudo")
            exit(1)

        ## TODO: handle just incase
        subprocess.run(["sudo", "chmod", "+x", pathfile], check=True)

    return


# Need the app to have executable permission
def get_app_icon(pathfile):
    print("he")


if len(sys.argv) != 2:
    print("Usage: addIcon <path_to_app_image>")
    exit(1)

pathfile = Path(sys.argv[1])

if not pathfile.exists() or not pathfile.is_file():
    print("File not specified or found in path")
    exit(1)

if pathfile.suffix != ".AppImage":
    print("File is not an AppImage")
    exit(1)

updated_file_name = strip_app_name(pathfile.stem)
updated_file_name_with_suffix = updated_file_name + ".AppImage"

renamed_pathfile = Path(
    pathfile.parent,
    updated_file_name_with_suffix,
)

pathfile.rename(renamed_pathfile)

executable_permission(pathfile)
