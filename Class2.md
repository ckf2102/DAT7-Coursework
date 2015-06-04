## Class 2
### 3 June 2015

**Cloning your repository from GitHub to your local machine (Git)**

```
$ git clone <url of repo>
$ cd RepoName

$ git remote -v
  # looking at remote aliases
  # way of identifying where to sync
  # remote alias: origin is a short cut for the <url> of your repo
  

# making changes to repo
$ git status
  # shows status of commits
$ git add * 
  # adding files to be committed
  # can use specific file name
$ git push origin master  # pushes to the origin the master file
```

- You clone repositories, not the files
- You also clone the histories
