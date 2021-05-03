0x15. API
=========

-   Foundations - System engineering & DevOps -- Scripting

Background Context
------------------

[![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210502%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210502T221356Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b7d9d73f3367fd0b9422e58816a51867a453763051ef896e6b9fc459e86bcf70)](https://youtu.be/-2kyU6-j8ZQ)

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them -- access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let's build Python scripts.

Resources
---------

**Read or watch**:

-   [Friends don't let friends program in shell script](https://intranet.hbtn.io/rltoken/6isWaTEpGTrwhzCCG5s_Tw "Friends don't let friends program in shell script")
-   [What is an API](https://intranet.hbtn.io/rltoken/I-XLIq5AwH-j29xJtzr6bQ "What is an API")
-   [What is an API? In English, please](https://intranet.hbtn.io/rltoken/I1nC8rhySGahG3gXYBfDPA "What is an API? In English, please")
-   [What is a REST API](https://intranet.hbtn.io/rltoken/0KygelrSeZsIujDu-I2a0w "What is a REST API")
-   [What are microservices](https://intranet.hbtn.io/rltoken/lewYS0z2RuFuiIkIgaCHSA "What are microservices")
-   [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.hbtn.io/rltoken/lEisphllQEYAs5yg26Ng0w "PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.hbtn.io/rltoken/NqyA8rE6iLsbRnZB0A6nuA "explain to anyone"), **without the help of Google**:

### General

-   What Bash scripting should not be used for
-   What is an API
-   What is a REST API
-   What are microservices
-   What is the CSV format
-   What is the JSON format
-   Pythonic Package and module name style
-   Pythonic Class name style
-   Pythonic Variable name style
-   Pythonic Function name style
-   Pythonic Constant name style
-   Significance of CapWords or CamelCase in Python

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   **Libraries imported in your Python files must be organized in alphabetical order**
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `PEP 8` style
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   You must use [get](https://intranet.hbtn.io/rltoken/nVy7hbvKVJkhr5LIHIsHSg "get") to access to dictionary value by key (it won't throw an exception if the key doesn't exist in the dictionary)
-   Your code should not be executed when imported (by using `if __name__ == "__main__":`)