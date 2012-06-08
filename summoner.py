import subprocess

# Internal - detects if the user has git
# 
# returns True if hub is being used, False otherwise
def detect_git():
    retcode = subprocess.call(["/usr/bin/which", "git"]) 
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
    print "detecting git..."
    print "attempting to detect hub..."
    has_hub = detect_hub()

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
    print
    print "getting templates" 
    print "    smnr <templatename>                   -> template into clipboard"
    print "    smnr <templatename> <filename>        -> template into file"
    print
    print "syncing"
    print "    smnr push                             -> pushes summoner templates to remote"
    print "    smnr pull                             -> pulls summoner templates to remote"
    print "    smnr pull <giturl>                    -> pulls summoner templates from someone elses remote"
