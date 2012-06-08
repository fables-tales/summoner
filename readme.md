This is summoner, a fast way to snippet and template

#Setup
* `smnr init` will interactively set you up!
* `smnr remote <giturl>` will change your summoner git url

#Create a template
* `smnr create <templatename>` will open your editor and create a template with that templatename for you. 
* `smnr create <templatename> <filename>` will create a template from the specified file name

#Modify existing templates
* `smnr update <templatename>` will open your editor and replace the template when you're done.

#Delete existing templates
* `smnr delete <templatename>` deletes a given template

#List templates
* `smnr list` lists all templates

**whenever you create or update templates you'll need to give a commit message. (summoner is powered by git)**

#Use a template
* `smnr <templatename>` will copy the template into your clipboard
* `smnr <templatename> <filename>` will push a template into the specified file

#Sync
* `smnr push` pushes your templates
* `smnr pull` pulls your templates
* `smnr pull <giturl>` pulls templates form someone elses repo
