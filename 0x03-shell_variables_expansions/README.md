0x03. Shell, init files, variables and expansions
=================================================

 Foundations - System engineering & DevOps -- Bash   [](https://intranet.hbtn.io/projects/209#)

Resources
---------

**Read or watch**:

-   [Expansions](https://intranet.hbtn.io/rltoken/G5p7gU70olYFxbN_DfuXpQ "Expansions")
-   [Shell Arithmetic](https://intranet.hbtn.io/rltoken/C2JAWjeSMt5I0EmuplF32A "Shell Arithmetic")
-   [Variables](https://intranet.hbtn.io/rltoken/zj7i19F9iE9eUdjBgR6C3Q "Variables")
-   [Shell initialization files](https://intranet.hbtn.io/rltoken/lHvzUhLmLgBVfsoJzYDj_w "Shell initialization files")
-   [The alias Command](https://intranet.hbtn.io/rltoken/5JiNabFuBFXpJKqGGh9EjQ "The alias Command")
-   [Technical Writing](https://intranet.hbtn.io/rltoken/yG1jmJxtf-0eALGmsrfIjA "Technical Writing")

**man or help**:

-   `printenv`
-   `set`
-   `unset`
-   `export`
-   `alias`
-   `unalias`
-   `.`
-   `source`
-   `printf`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/RGfPlEf4sN0nswOChL6LCg "explain to anyone"), **without the help of Google**:

### General

-   What happens when you type `$ ls -l *.txt`

### Shell Initialization Files

-   What are the `/etc/profile` file and the `/etc/profile.d` directory
-   What is the `~/.bashrc` file

### Variables

-   What is the difference between a local and a global variable
-   What is a reserved variable
-   How to create, update and delete shell variables
-   What are the roles of the following reserved variables: HOME, PATH, PS1
-   What are special parameters
-   What is the special parameter `$?`?

### Expansions

-   What is expansion and how to use them
-   What is the difference between single and double quotes and how to use them properly
-   How to do command substitution with `$()` and backticks

### Shell Arithmetic

-   How to perform arithmetic operations with the shell

### The `alias` Command

-   How to create an alias
-   How to list aliases
-   How to temporarily disable an alias

### Other `help` pages

-   How to execute commands from a file in the current shell

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your scripts will be tested on Ubuntu 14.04 LTS
-   All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
-   All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789))
-   The first line of all your files should be exactly `#!/bin/bash`
-   A `README.md` file, at the root of the folder of the project, describing what each script is doing
-   You are not allowed to use `&&`, `||` or `;`
-   You are not allowed to use `bc`, `sed` or `awk`
-   All your files must be executable

More Info
---------

Read your `/etc/profile`, `/etc/inputrc` and `~/.bashrc` files.

Look at some files in the `/etc/profile.d` directory.

Note: You do not have to learn about `awk`, `tar`, `bzip2`, `date`, `scp`, `ulimit`, `umask`, or shell scripting, yet.