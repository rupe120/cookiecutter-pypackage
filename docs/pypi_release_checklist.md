# PyPI Release Checklist

## For Every Release

0. Check out release branch, merge all changes from master/main to release

1. Run the tests:

    > ``` bash
    > tox
    > ```

2. Update HISTORY.md

    Be noticed that github workflow will generate a changelog for you automatically.

3. Commit the changes:

    > ``` bash
    > git add HISTORY.md
    > git commit -m "Changelog for upcoming release 0.1.1."
    > ```

4. Update version number. The following are the actions taken in the `push-version.ps1` script at the root of the repository.

    > ``` powershell
    > {% include-markdown "../push-version.ps1" %}
    > ```

5. Check the PyPI listing page to make sure that the README, release
    notes, and roadmap display properly. If tox test passed, this should be ok, since
    we have already run twine check during tox test.

## About This Checklist

This checklist is adapted from:

- <https://gist.github.com/audreyr/5990987>
- <https://gist.github.com/audreyr/9f1564ea049c14f682f4>

It assumes that you are using all features of CookieCutter PyPackage.
