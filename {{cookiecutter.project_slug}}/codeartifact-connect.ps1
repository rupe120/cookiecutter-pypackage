param(
    [Parameter(Mandatory)]
    [string]$awsprofile
)

aws codeartifact login --tool pip --domain innovative-core --repository innovative-pip --profile $awsprofile