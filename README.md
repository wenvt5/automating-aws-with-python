# automating-aws-with-python

Repository for the A Cloud Guru course

## set up the environment (windows)
1. Run powershell as administrator to install software (linux terminal)
2. Chocolatey: https://chocolatey.org/
  - To install the rest
3. Atom
  - Or another text editor
  - `choco install atom -y`
  - to install atom on Centos
     - yum install wget git -y
     - wget https://github.com/atom/atom/releases/download/v1.18.0/atom.x86_64.rpm
     - yum localinstall atom.x86_64.rpm -y
4. Python 3
  - `choco install python3 -y`
5. NodeJS
  - `choco install nodejs -y`
6. AWS CLI
  - `choco install awscli -y`
7. Git
  - `choco install git -y /GitAndUnixToolsOnPath`
8. OpenSSH
  - `choco install openssh -y -params "/SSHAgentFeature"`
  - Or if that doesn't work:
  - `choco install openssh -y`
9. Restart windows
10. Serverless
  - `npm install -g serverless`
11. Pipenv
  - `pip3 install pipenv`
12. Generate SSH key:
  - `ssh-keygen -C <email>`

## 01-webotron

Webotron is a script that will sync a local directory to an S3 bucket, and optionally configure Route 53 and cloudfront as well.

### Features

Webtron currently has the following features:

- List buckets
- List contents of a bucket
- Create and set up bucket
- sync directory tree to bucket
- Set AWS profile with --profile = <profileName>
