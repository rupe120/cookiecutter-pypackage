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

4. Update version number. The following are an example of executing and the contents of the `push-version.ps1` script at the root of the repository.

    > ``` powershell
    > .\push-version.ps1 0.1.1 "documentation updates"
    > ```

    ``` powershell

    {% include-markdown "../push-version.ps1" %}
    
    ```

5. Check the CodeArtifact listing page to make sure that the README, release
    notes, and roadmap display properly. If tox test passed, this should be ok, since
    we have already run twine check during tox test.

