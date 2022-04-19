import os
import sys

def main():
    cwd = os.path.dirname(__file__)
    package_dir = None

    if sys.argv[0] == "in-place":
        # Skip the project folder
        package_dir = os.path.abspath(os.path.join(cwd, "../{{cookiecutter.project_slug}}/"))

    elif len(sys.argv) > 1:        
        print("Unknown argument(s)")
        print(sys.argv[1:])

    else:
        package_dir = os.path.abspath(os.path.join(cwd, "../"))

    if package_dir:
        os.system(f"cookiecutter {package_dir}")