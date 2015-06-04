## Class 2
### 3 June 2015

# GitHub -> Git -> GitHub

*Cloning your repository from GitHub to your local machine (Git)*

```
$ git clone <url of repo>
$ cd RepoName
```

```
$ git remote -v
```
- Looking at remote aliases
- Way of identifying where to sync
- Remote alias: origin is a short cut for the <url> of your repo
- Clone automatically assumes you want origin remote alias
- Remotes are repo-specific
  
*Making changes, checking your status*


```
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
