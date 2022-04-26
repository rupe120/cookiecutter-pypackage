# Tutorial

???+ Feedback
    Did you find this article confusing? [Edit this file] and pull a request!

To start with, you will need [GitHub], [Pypi] , [TestPyPi] and [Codecov] account. If you don't have one, please follow the links to apply one before you get started on this tutorial.

If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at [GitHub Help]

## Step 1: Install Python Project Wizard (aws-ppw)

Install aws-ppw:

``` bash
pip install aws-ppw
```

## Step 2: Generate Your Package

Now it's time to generate your Python package.

Run the following command and feed with answers:

``` bash
aws-ppw
```

Finally a new folder will be created under current folder, the name is the answer you provided to `project_slug`.

The contents layout should looks like:

``` console
.
├── AUTHORS.md
├── CONTRIBUTING.md
├── .coveragerc
├── dist
├── docs
│   ├── api.md
│   ├── authors.md
│   ├── contributing.md
│   ├── history.md
│   ├── index.md
│   ├── installation.md
│   └── usage.md
├── .editorconfig
├── .flake8
├── .git
├── .github
│   ├── ISSUE_TEMPLATE.md
│   └── workflows
│       ├── dev.yml
│       └── release.yml
├── .gitignore
├── HISTORY.md
├── .isort.cfg
├── LICENSE
├── mkdocs.yml
├── poetry.lock
├── ppw_0420_01
│   ├── __init__.py
│   ├── cli.py
│   └── ppw_0420_01.py
├── .pre-commit-config.yaml
├── pyproject.toml
├── pyrightconfig.json
├── README.md
├── site
├── tests
│   ├── __init__.py
│   └── test_ppw_0420_01.py
└── tox.ini
```

Here the project_slug is ppw_0420_01, when you generate yours, it could be other name.

Also be noticed that there's pyproject.toml in this folder. This is the main configuration file of our project.

## Step 3: Build a Virtual Environment and Install Dev Requirements

You should still be in the folder named as `project_slug`, which containing the `pyproject.toml` file.

Install the new project's local development requirements inside a virtual environment:

``` bash
pip install poetry
poetry install -E dev
tox
```

We start with install poetry, since the whole project is managed by poetry. Then we installed extra dependency need by developer, such as documentation build tools, lint, formatting and test tools etc.

We also launch a smoke test here by running `tox`. This will give you a test report and lint report. You should see no errors except some lint warnings.

### Extra dependencies

  Extra dependencies are grouped into the dev group. When you ship the package, dependencies in this group might not be shipped.
  
  As the developer, you will need install all the dependencies.

### Tox errors

  if you found errors like the following during tox run:

  ``` console
  ERROR: InterpreterNotFound: python3.9
  ```
  
  don't be panic, this is just because python3.x is not found on your machine. If you decide to support that version of Python in your package, please install it on your machine. Otherwise, remove it from tox.ini and pyproject.toml (search python3.x then remove it).

## Step 4: Create a GitHub Repo

Go to your GitHub account and create a new repo named `mypackage`, where `mypackage` matches the `[project_slug]` from your answers to running cookiecutter.

Then goto repo > settings > secrets, click on 'New repository secret', add the following
 secrets:

- DEV_CODEARTIFACT_ROLE_ARN (Required for AWS access. May already be set as an organization secret.)
- PROD_CODEARTIFACT_ROLE_ARN (Required for AWS access. May already be set as an organization secret.)

## Step 6: Set Up codecov integration

### Confirm

  If you have already setup codecov integration and configured access for all your repositories, you can skip this step.

### Setup

In your browser, visit [install codecov app], you'll be landed at this page:

![CodeCov install](http://images.jieyu.ai/images/202104/20210419175222.png)

Click on the green `install` button at top right, choose `all repositories` then click
on `install` button, following directions until all set.

## Step 7: Upload code to github

Back to your develop environment, find the folder named after the `[project_slug]`. Move into this folder, and then setup git to use your GitHub repo and upload the code:

``` bash
cd mypackage

git add .
git commit -m "Initial skeleton."
git branch -M main
git remote add origin git@github.com:myusername/mypackage.git
git push -u origin main
```

Where `myusername` and `mypackage` are adjusted for your username and package name.

You'll need an ssh key to push the repo. You can [Generate] a key or [Add] an existing one.

### Notice

  if you answered 'yes' to the question if install pre-commit hooks at last step, then you should find pre-commit be invoked when you run `git commit`, and some files may be modified by hooks. If so, please add these files and **commit again**.

### Check result

  After pushing your code to github, goto github web page, navigate to your repo, then click on actions link, you should find screen like this:

  ![GitHub Workflows](http://images.jieyu.ai/images/202104/20210419170304.png)

  There should be one workflow running. After it finished, go to the test [CodeArtifact] repository, check if a new artifact is published under the name {{ cookiecutter.project_slug }}

## Step 8. Check documentation

Documentation will be published and available at <https://{your_github_account}.github.io/{your_repo}> once:

1. the branch is release
2. the commit is tagged, and the tag name is started with 'v' (lower case)
3. build/testing executed by github CI passed

If you'd like to see what it's look like now, you could run the following command:

``` console
mkdocs gh-deploy
```

then check your documentation at <https://{your_github_account}.github.io/{your_repo}>

## Step 9. Make official release

After done with your phased development, switch to release branch, following instructions at [release checklist](/pypi_release_checklist), trigger first official release and check result in [CodeArtifact].

[Edit this file]: https://github.com/innovativeSol/innovative-pip-cookiecutter-pypackage/blob/master/docs/tutorial.md
[poetry]: https://python-poetry.org/
[Codecov]: https://codecov.io/
[CodeArtifact]: https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html
[GitHub]: https://github.com/
[GitHub Help]: https://help.github.com/
[Generate]: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
[Add]: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
[How to apply personal token]: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token
[install codecov app]: https://github.com/apps/codecov
