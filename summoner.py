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
