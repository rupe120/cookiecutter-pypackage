import os
import sys

def main():
    cwd = os.path.dirname(__file__)
    package_dir = None
    if sys.argv[0] == "in-place":
        package_dir = os.path.abspath(os.path.join(cwd, "../"))
    elif len(sys.argv) > 0:
        print("Invalid argument(s)")
        print(sys.argv)
    else:
        package_dir = os.path.abspath(os.path.join(cwd, "../{{cookiecutter.project_slug}}/"))

    if package_dir:
        os.system(f"cookiecutter {package_dir}")