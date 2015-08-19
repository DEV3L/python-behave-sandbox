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
2. (OPTION A) Create a Python virtualenv for this project
    * mkvirtualenv python-behave-sandbox
    * Install behave
        * <http://pythonhosted.org/behave/install.html>
        * pip install behave
4. (OPTION B) From Pycharm
    * Create a virtualenv
        * <https://www.jetbrains.com/pycharm/help/creating-virtual-environment.html>
    * From the Settings -> Project Interpreter click the "+" icon
        * Search for "behave"
        * Click the Install Package button
