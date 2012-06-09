import subprocess
import sys
import os

# Public - creates the summoner repo
# 
# has_hub - whether or not the user has the hub command 
#
# Returns nothing
def create_repo(has_hub):
    pass

# Public - determines the location of the summoner repo
#
# returns None if the repo doesn't exist, otherwise the path to it
def locate_summoner_repo():
    REPO_PATH = "~/.summoner/repo"
    if os.path.exists(REPO_PATH):
        return REPO_PATH
    else:
        return None
    

# Internal - detects if the user has git
# 
# returns True if hub is being used, False otherwise
def detect_git():
    retcode = subprocess.call(["/usr/bin/which", "git"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    if retcode == 0:
        return True
    else:
        return False

# Internal - detects if the user is using github's hub plugin or bare git
#
# returns true if hub is being used, false otherwise
def detect_hub():
    retcode = subprocess.call(["/usr/bin/which", "hub"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if retcode == 0:
        return True
    else:
        return False


# Public - interactively initialises the summoner system
#
# returns nothing
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
        sys.stdout.write("                       [ok]\n")

    else:
        sys.stdout.write("  [yes]\n")

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
