##Class 3
###8 June 2015

**Assorted Git Tips**

[Last 4 slides] (https://github.com/justmarkham/DAT7/blob/master/slides/02_git_github.pdf)

Deleting or moving a repo
- Settings, then Delete
- Delete a local repo: just delete the folder

Gists: lightweight repos
- easy way to add text
- creates a github repository
- makes it easy to share codefiles with just the url
- also useful if you've screwd up your github repo and you need to submit hw...

Excluding files from a repo
- ".gitignore"
- don't want Git to track
	- large file, secret code...
```
$ touch *.gitignore
```

Initializing Git locally
- want to start tracking with git?
- still can't create from command line
```
$ git init
	# create a repo on GitHub (without a README)
$ git remote add origin <URL>
```

