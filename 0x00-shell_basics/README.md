0x00. Shell, basics
===================

 Foundations - System engineering & DevOps -- Bash   [](https://intranet.hbtn.io/projects/205#)

Resources
---------

**Read or watch**:

-   [What Is "The Shell"?](https://intranet.hbtn.io/rltoken/pn2_LGNuA1yFY7zy3CQmig "What Is "The Shell"?")
-   [Navigation](https://intranet.hbtn.io/rltoken/Hh8elGgCpj--6othR7S7GQ "Navigation")
-   [Looking Around](https://intranet.hbtn.io/rltoken/84xsZOempqy5I7ZkueeIsg "Looking Around")
-   [A Guided Tour](https://intranet.hbtn.io/rltoken/Jp1c4V3hJiGBuVzYCtnQKw "A Guided Tour")
-   [Manipulating Files](https://intranet.hbtn.io/rltoken/wFwFXKQmSpmxYyvHvCIC-Q "Manipulating Files")
-   [Working With Commands](https://intranet.hbtn.io/rltoken/Aq3NVLBhgnQS6NYtHI8i4w "Working With Commands")
-   [Reading Man pages](https://intranet.hbtn.io/rltoken/RohkjGiQtMHgPfj0N_k1Bw "Reading Man pages")
-   [Keyboard shortcuts for Bash](https://intranet.hbtn.io/rltoken/0HvJ2B_wSl6Oyshcn-OHrg "Keyboard shortcuts for Bash")
-   [LTS](https://wiki.ubuntu.com/LTS)
-   [Shebang](https://intranet.hbtn.io/rltoken/ketzZf-802Fb-mSGkyPa4w "Shebang")

**man or help**:

-   `cd`
-   `ls`
-   `pwd`
-   `less`
-   `file`
-   `ln`
-   `cp`
-   `mv`
-   `rm`
-   `mkdir`
-   `type`
-   `which`
-   `help`
-   `man`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/VCja0ArJiqJAMEzE-01dSA "explain to anyone"), **without the help of Google**:

### General

-   What does RTFM mean?
-   What is a Shebang

### What is the Shell

-   What is the shell
-   What is the difference between a terminal and a shell
-   What is the shell prompt
-   How to use the history (the basics)

### Navigation

-   What do the commands or built-ins `cd`, `pwd`, `ls` do
-   How to navigate the filesystem
-   What are the . and .. directories
-   What is the working directory, how to print it and how to change it
-   What is the root directory
-   What is the home directory, and how to go there
-   What is the difference between the root directory and the home directory of the user root
-   What are the characteristics of hidden files and how to list them
-   What does the command `cd -` do

### Looking Around

-   What do the commands `ls`, `less`, `file` do
-   How do you use options and arguments with commands
-   Understand the ls long format and how to display it
-   [A Guided Tour](https://intranet.hbtn.io/rltoken/Jp1c4V3hJiGBuVzYCtnQKw "A Guided Tour")
-   What does the `ln` command do
-   What do you find in the most common/important directories
-   What is a symbolic link
-   What is a hard link
-   What is the difference between a hard link and a symbolic link

### Manipulating Files

-   What do the commands `cp`, `mv`, `rm`, `mkdir` do
-   What are wildcards and how do they work
-   How to use wildcards

### Working with Commands

-   What do `type`, `which`, `help`, `man` commands do
-   What are the different kinds of commands
-   What is an alias
-   When do you use the command help instead of man

### Reading Man Pages

-   How to read a man page
-   What are man page sections
-   What are the section numbers for User commands, System calls and Library functions

### Keyboard Shortcuts for Bash

-   Common shortcuts for Bash

### LTS

-   What does `LTS` mean?

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 14.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file at the root of the `holberton-system_engineering-devops` repo, containing a description of the repository
-   A `README.md` file, at the root of the folder of *this* project, describing what each script is doing
-   You are not allowed to use backticks, `&&`, `||` or `;`
-   All your scripts must be executable. To make your file executable, use the `chmod` command: `chmod u+x file`. Later, we'll learn more about how to utilize this command.
