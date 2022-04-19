param(
    [Parameter(Mandatory)]
    [string]$version,
    [Parameter(Mandatory)]
    [string]$message
)

poetry version $version
git add -A
git commit -m "v$version"
git tag v$version -m $message
git push --atomic origin master v$version