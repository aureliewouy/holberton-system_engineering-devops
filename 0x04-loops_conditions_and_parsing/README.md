0x04. Loops, conditions and parsing
===================================

 Foundations - System engineering & DevOps -- Bash   [](https://intranet.hbtn.io/projects/251#)

*For this project, students are expected to look at this concept:*

-   *[Shell](https://intranet.hbtn.io/concepts/9)*

Background Context
------------------

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/b07e3333b1edfb9beed5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210222%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210222T174744Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2de89001d1dab76d6d140f4fbb8969783c7924763de3c770ae3aed8fb1710b1d)](https://youtu.be/BC2neyc5GcI)

Resources
---------

**Read or watch**:

-   [Loops sample](https://intranet.hbtn.io/rltoken/XnVjFM8a1W4RfRu4TCPY-g "The <code>for</code> loop" target="_blank">The <code>for</code> loop</a> </li>
    <li><a href=")
-   [Variable assignment and arithmetic](https://intranet.hbtn.io/rltoken/IM0Gv6VPzwAmqzlJxETZkw "Variable assignment and arithmetic")
-   [Comparison operators](https://intranet.hbtn.io/rltoken/K3E6xI9-goDM-93vsjCpPA "Comparison operators")
-   [File test operators](https://intranet.hbtn.io/rltoken/0OZLLDT28KrRZdid-l6hwg "File test operators")
-   [Make your scripts portable](https://intranet.hbtn.io/rltoken/Dyrnap2UC-LrzrmCOJRx8A "Make your scripts portable")

**man or help**:

-   `env`
-   `cut`
-   `for`
-   `while`
-   `until`
-   `if`

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/gshUY8R5dEKQKBBvTTGAbQ "explain to anyone"), **without the help of Google**:

### General

-   How to create SSH keys
-   What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
-   How to use `while`, `until` and `for` loops
-   How to use `if`, `else`, `elif` and `case` condition statements
-   How to use the `cut` command
-   What are files and other comparison operators, and how to use them

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted on Ubuntu 14.04 LTS
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   You are not allowed to use `awk`
-   Your Bash script must pass `Shellcheck` (version `0.3.3-1~ubuntu14.04.1` via `apt-get`) without any error
-   The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
-   The second line of all your Bash scripts should be a comment explaining what is the script doing

More Info
---------

### Shellcheck

[Shellcheck](https://intranet.hbtn.io/rltoken/E7Pr2zeM3cdY5-C0HKwtbw "Shellcheck") is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. `Shellcheck` is your friend! **All your Bash scripts must pass `Shellcheck` without any error or you will not get any points on the task**.

`Shellcheck` is available on the school's computers. If you want to use it on your own computer, here is how to [install it](https://intranet.hbtn.io/rltoken/SOX0HZTMgzHbcxrvU1X4hw "install it").