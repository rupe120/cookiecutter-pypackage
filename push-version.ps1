param(
    [Parameter(Mandatory,
        HelpMessage="Enter a valid version number #.#.#")]
    [ValidatePattern("(\d+\.)?(\d+\.)?(\d+)")]
    [string]$version,
    [Parameter(Mandatory)]
    [string]$message
)

poetry version $version
git add -A
git commit -m "v$version"
git tag v$version -m $message
git push --atomic origin master v$version