param{
    [Parameter()]
    [string]$version
    [string]$description
}

poetry version $version
git add -A
git commit -m "v$version"
git tag v$version -m $description
git push --atomic origin master v$version