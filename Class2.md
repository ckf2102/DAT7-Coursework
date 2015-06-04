## Class 2
### 3 June 2015

- You clone repositories, not the files
- You also clone the histories

**GitHub -> Git -> GitHub**

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
$ git status
  # shows status of commits
```
- File statuses (possible color-coded):
  - Untracked (red)
    - You need to tell Git what you want to track
  - Tracked and modified (red)
  - Staged for committing (green)
  - Committed

```
$ start readme.md
  # opens the text editor straight from command line
```

*Pushing your edits from Git to GitHub*
```
$ git add * 
```
- Add = track the specific (or all) files
- Committing is a completely different step!!

```
$ git commit -m "your message for commit"
```
- You have now committed a change
- NOTHING HAS HAPPENED ON GITHUB! Does not automatically sync

```
$ git push origin master  # pushes to the origin the master file
```
- Pushes the changes
- Master is the name of the branch (name Master by default)

*Quick Recap*
- Created a repo on GitHub
- Cloned repo to your local computer (git clone)
	- Automatically setes up your "origin" remote
- Made fle changes
- Staged changes for committing (git add)
- Committed changes (git commit)
- Pushed changes to GitHub (git push)
- Inspected along the way (git remote, git status, git log)
- Can't really create a repo in just Git
- Easier to create the repo in GitHub first

*Pulling Changes*
- Repo changes have been made on local machine and then pushed
- Git does not automatically pull changes from your repo
- Need to manually pull changes from remote locations
- Like syncing local files from Dropbox

```
$ git pull origin master
```
- Generally we will only be doing pushes for our own repo
- We will be pulling from the DAT7 repo
- Clone is the initializing --> after that, you can just pull
