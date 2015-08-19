# python-behave-sandbox
This is a repository for me understanding how to use behave for behaviour-driven development, Python style.

<https://pythonhosted.org/behave/>

The project setup steps are target for a Linux Ubuntu VirtualBox VM, but with some slight tweaks it should work on any OS.

* Download and install VirtualBox
    * <https://www.virtualbox.org/wiki/Downloads>
* Download Ubuntu ISO
    * <http://www.ubuntu.com/download/desktop>

## Prerequisites
* Python installed
    * <https://www.python.org/downloads/>
    * Able to run "pip" command through console
* Virtualenv installed
    * <https://virtualenv.pypa.io/en/latest/>
    * sudo pip install --upgrade pip virtualenv virtualenvwrapper

#Usage/Setup Instructions
1. From command line retrieve project from GitHub
	* git clone https://github.com/DEV3L/python-behave-sandbox.git
2. Create a Python virtualenv for this project
    * mkvirtualenv python-behave-sandbox
    * Install behave
        * <http://pythonhosted.org/behave/install.html>
        * pip install behave
4. (OPTIONAL) From Pycharm
    * Create a virtualenv
        * <https://www.jetbrains.com/pycharm/help/creating-virtual-environment.html>
    * From the Settings -> Project Interpreter click the "+" icon
        * Search for "behave"
        * Click the Install Package button

#Run Instructions
```
# From command line within project source directory
workon python-behave-sandbox
cd 01_hello_world
behave

###
# Feature: showing off behave # features/everything.feature:1
#
#  Scenario: run a simple test        # features/everything.feature:3
#    Given we have behave installed   # features/steps/steps.py:4 0.000s
#    When we implement a test         # features/steps/steps.py:10 0.000s
#    Then behave will test it for us! # features/steps/steps.py:16 0.000s
# 
# 1 feature passed, 0 failed, 0 skipped
# 1 scenario passed, 0 failed, 0 skipped
# 3 steps passed, 0 failed, 0 skipped, 0 undefined
# Took 0m0.000s
```
