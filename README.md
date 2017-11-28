# Chaos Systems RPM Repository

## Building with the docker image
### docker-compose.override.yml
There are some things that need to be overridden to match your individual environment, your overrides file should not be checked into git.

```
version: "3.3"

# You need to set the profile that you use for accessing the aws account.
services:
  rpm:
    environment:
      - AWS_DEFAULT_PROFILE: [profile]
```

## Bootstrapping an OS

### RPM
`rpm -ivh https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

### DNF
`dnf install -y https://s3-eu-west-1.amazonaws.com/chaossystems-repositories/artifacts/rpm/chaossystems/noarch/chaossystems-repos-1.0-1.noarch.rpm`

## Reference
Most of this was taken from the examples in [this blog post](http://blog.celingest.com/en/2014/09/17/create-your-own-yum-rpm-repository-using-amazon-s3/)
