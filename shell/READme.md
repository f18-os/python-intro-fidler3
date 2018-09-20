# Shell lab

In this lab we were instructed to create a shell that could handle simple
shell commands suchs "cd", "ls", "cat. We were also suppose create functions
that could also handle redirecteion and PIP.

# To Run

python3 shell.py

This program requires python 3

# redirect

The redirect function allows a simple command's output to be redirected into a
different file. We use a fork command to create a subprocess and the exec and
environ commands to run basic functions the shell would run otherwise.

# simplecommands

The simple command functions handle simple line functions such as "ls" and cat
<file>. Similarly to how a redirection happens.

# PIP

Unfortunately at the moment I was unable to properly get a PIP to work. My
problem was getting the parallel process to work using fork operation. I think
I just need more time then usual to fully understand how to write it out. I
know I need two forks, to run simultaenously and I need the outputting
proccess to wait on the child process to finish to include it in its own
output....TO BE CONTINUED
