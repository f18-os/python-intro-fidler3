
#! /usr/bin/env python3

import os, sys, time, re

def redirect(command):

    pid = os.getpid()               # get and remember pid

    #os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
       # os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
       #          (os.getpid(), pid)).encode())
        args = command
        #print(*args , sep = " " )
        os.close(1)                 # redirect child's stdout
        sys.stdout = open(command[3], "w") # os.open("p4-output.txt", os.O_CREAT)
        os.set_inheritable(1, True)
        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[0])
            try: 
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly 

        os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)                 # terminate with error

    else:                           # parent (forked ok)
        #os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
#                 (pid, rc)).encode())
        childPidCode = os.wait()
        #os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
 #                childPidCode).encode())

def simplecommands(args):
    pid = os.getpid()               # get and remember pid

    #os.write(1, ("About to fork (pid=%d)\n" % pid).encode())
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:                   # child
     #   os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" % 
        #         (os.getpid(), pid)).encode())
        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[0])
            try: 
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly 

        os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)                 # terminate with error

    else:                           # parent (forked ok)
      #  os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" % 
         #        (pid, rc)).encode())
        childPidCode = os.wait()
        #os.write(1, ("Parent: Child %d terminated with exit code %d\n" % 
 #                childPidCode).encode())


#this function is still a work in progress
# Advise not to run
# file descripter error
def PIP(args):
    pid = os.getpid()
    print(args)
    cmds = [args[0], args[1]] #split commands
    cmd2 = [args[3], args[4]]
    pr,pw = os.pipe() #pipe read, pipe write

    for f in (pr, pw):
        os.set_inheritable(f, True)
    print("pipe fds: pr=%d, pw=%d" % (pr, pw))

    import fileinput

    print("About to fork (pid=%d)" % pid)

    rc = os.fork()

    if rc < 0:
        print("fork failed, returning %d\n" % rc, file = sys.stderr)
        sys.exit(1)
        
    elif rc == 0:                   #  child - will write to pipe
        print("Child: My pid==%d.  Parent's pid=%d" % (os.getpid(), pid), file=sys.stderr)
        os.close(1) # redirect child's stdout
       # d = os.fork()
       # if d == 0:
            #some sort of parellism needs to go on...
        os.dup(pw)
        for fd in (pr, pw):
            os.close(fd)
        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, args[3])
            try: 
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly
        exit()
 
    else:                           # parent (forked ok)
        print("Parent: My pid==%d.  Child's pid=%d" % (os.getpid(), rc), file=sys.stderr)
        os.close(0)
        os.dup(pr)
        for fd in (pw, pr):
            os.close(fd)
        for line in fileinput.input():
            print("From child: <%s>" % line)

#change directory
def changeDirectory(path):
    try:
        os.chdir(path)
    except FileNotFoundError: #if path does not exist
        print("No such path in the directory")
        pass
    
while 1: #main--- userinput
    try:
        userinput = input("$ ")
    except EOFError:
        print("\n")
        sys.exit()
    ui = userinput.split()
    if(userinput == "exit"):
            sys.exit()
    elif(ui[0] == "cd"):
        changeDirectory(ui[1])
    elif(">" in userinput):
        #userinput.split(">")
        redirect(ui)
    elif("|" in userinput):
        #userinput.split("|")
        PIP(ui)
    else:
        simplecommands(ui)
  
    
