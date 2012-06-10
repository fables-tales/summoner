import subprocess
import sys
import os

home_dir = os.environ["HOME"]
SUMMONER_PATH = home_dir + "/.summoner"
REPO_PATH = home_dir + "/.summoner/summoner_repo"

# Public - creates the summoner repo
# 
# has_hub - whether or not the user has the hub command 
#
# Returns nothing
def create_repo(has_hub):
    os.mkdir(SUMMONER_PATH)
    os.mkdir(REPO_PATH)
    subprocess.call(["git","init"], cwd=REPO_PATH)
    if (has_hub):
        print
        wants_hub = raw_input("do you want me to create a repo on github for you? [y/n] ")
        if wants_hub.find("y") != -1:
            subprocess.call(["hub","create"], cwd=REPO_PATH)

# Public - determines the location of the summoner repo
#
# Returns None if the repo doesn't exist, otherwise the path to it
def locate_summoner_repo():
    if os.path.exists(REPO_PATH):
        return REPO_PATH
    else:
        return None

# Internal - detects if the user has git
# 
# Returns True if hub is being used, False otherwise
def detect_git():
    retcode = subprocess.call(["/usr/bin/which", "git"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    if retcode == 0:
        return True
    else:
        return False

# Internal - detects if the user is using github's hub plugin or bare git
#
# Returns true if hub is being used, false otherwise
def detect_hub():
    retcode = subprocess.call(["/usr/bin/which", "hub"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if retcode == 0:
        return True
    else:
        return False

# Public - interactively initialises the summoner system
#
# Returns nothing
def init():
    sys.stdout.write("detecting git...")
    sys.stdout.flush()
    has_git = detect_git()
    if not has_git:
        print "ZOMG you don't have git :("
        print "install it, then use summoner!"
        sys.exit(1)
    else:
        sys.stdout.write("                       [ok]\n")

    sys.stdout.write("detecting hub...")
    sys.stdout.flush()
    has_hub = detect_hub()
    if not has_hub:
        sys.stdout.write("                       [nope]\n")
    else:
        sys.stdout.write("                       [ok]\n")

    sys.stdout.write("does the summoner repo already exist?")
    repo_path = locate_summoner_repo()
    if repo_path is None:
        sys.stdout.write("  [no]\n")
        sys.stdout.write("creating repo...")
        create_repo(has_hub)
        sys.stdout.write("repo created successfully\n")

        sys.stdout.write("you're ready to summon!\n")
    else:
        sys.stdout.write("  [yes]\n")

# Public - checks if a template exists
#
# templatename - the name of the template to check for existance
#
# Examples
#
#   template_exists("html/index.html")
#   # => False
#
# Returns true if the template exists, false otherwise
def template_exists(templatename):
    return os.path.exists(REPO_PATH + "/" + templatename)

# Public - edits a template
#
# templatename - the name of the template to edit
#
# Returns nothing
def edit(templatename):
    path = REPO_PATH + "/" + filename
    if not os.path.exists(os.path.dirname(path)):
        subprocess.call(["mkdir","-p",os.path.dirname(path)])

    editor = os.environ["EDITOR"]
    subprocess.call([editor + " " + filename], cwd=REPO_PATH, shell=True)

# Internal - commits a template
# 
# templatename - the name of the template to edit 
#
# Returns nothing
def commit(templatename):
    if template_exists(templatename):
        subprocess.call(["git", "add", templatename], cwd=REPO_PATH)
        subprocess.call(["git", "commit"], cwd=REPO_PATH)

# Public - creates a template interactively
#
# templatename - the name of the template to create 
#
# Returns nothing
def create(templatename):
    if template_exists(templatename):
        print "This template already exists!"
        print "Did you want to modify instead?"
    else:
        edit(templatename)
        commit(templatename)

# Public - prints usage information for summoner
#
# Returns nothing
def usage():
    print "usage is one of"
    print "setup commands"
    print "    smnr init                             -> interactive setup"
    print "    smnr remote <giturl>                  -> sets your smnr remote"
    print 
    print "template modification"
    print "    smnr create <templatename>            -> creates a template interactively"
    print "    smnr create <templatename> <filename> -> creates a template with a file"
    print "    smnr update <templatename>            -> interactively updates a template"
    print "    smnr delete <templatename>            -> deletes a specified template"
    print "    smnr list                             -> lists all templates"
    print
    print "getting templates" 
    print "    smnr <templatename>                   -> template into clipboard"
    print "    smnr <templatename> <filename>        -> template into file"
    print
    print "syncing"
    print "    smnr push                             -> pushes summoner templates to remote"
    print "    smnr pull                             -> pulls summoner templates to remote"
    print "    smnr pull <giturl>                    -> pulls summoner templates from someone elses remote"
