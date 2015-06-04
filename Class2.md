## Class 2
### 3 June 2015

**Command Lines**

[New Features](https://github.com/justmarkham/DAT7/blob/master/code/02_command_line.md)

- Working at the command line is a benefit if you're working with large files

More fun stuff
```
$ head sms.tsv
	# defaults to first 10 lines
$ head -n5 sms.tsv
	# only first five
$ tail sms.tsv

$ cat sms.tsv
	# if you hit ctrl-c then it'll stop

$ wc sms.tsv
	# lines, words, characters
	# Word Count
$ wc -l sms.tsv
	# just lines, can also use -w, -c

$ find
	# finding files by name
	# will show the file path

$ grep 'lol' sms.tsv
	# case sensitive
	# g stands for global! so best to direct it to a specific directory...
	
$ grep -i 'where are you' sms.tsv
	# now not case sensitive
	# ignore case

$ grep -r 'where are you' .
	# searches in the current directory (that's what the period is for)
	# recursive

$ grep --help
	# see all commands and options
```

Cool symbols
- | --> pipe... pipe output from one command to input of another command
- > --> sends the results to a file
- >> --> appends to a file
```
$ grep -i 'lol' sms.tsv
$ grep -i 'lol' sms.tsv | head
	# now only see the first ten lines of texts with 'lol'

$ grep -i 'lol' sms.tsv | ws -l
	# number of lines that have 'lol'... more useful

$ grep -i 'lol' sms.tsv > lol.txt
	# can give it a path if you want

$ grep -i 'hahaha' sms.tsv >> lol.txt
	# appends! better than > because then you can't accidentally overwrite a file
```

**GitHub -> Git -> GitHub**

- You clone repositories, not the files
- You also clone the histories

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

*Merge Conflicts*
- Before you edit any DAT7 files, copy them elsewhere first and make edits to those copies
	- If Kevin makes any edits while I'm making edits, there are going to be problems...
