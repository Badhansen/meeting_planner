# meeting_planner
A simple project for maintaining meetings.
# Installation Procedure 
Hello! I am describing the **Windows** installation procedure, if you have **Mac** or **Linux** please follow this link [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
to setup you project.
# Windows
The Python installers for Windows include pip. You should be able to access pip using:
```
py -m pip --version
```
You can make sure that pip is up-to-date by running:
```
py -m pip install --upgrade pip
```
If you get this error
```diff
- Could not install packages due to an EnvironmentError: [WinError 5] Access is denied: 'c:\\program files (x86)\\microsoft visual studio\\shared\\python37_64\\lib\\site-packages\\pip-19.0.3.dist-info\\entry_points.txt'
- Consider using the `--user` option or check the permissions.
```
Then use the following command or run command line as administrator and run the previous command that also work.
```
py -m pip install --user --upgrade pip
```
# Installing virtualenv
virtualenv is used to manage Python packages for different projects. Using virtualenv allows you to avoid installing Python packages globally which could break system tools or other projects. You can install virtualenv using pip.
```
py -m pip install --user virtualenv
```
# Setup project
First create a directory  
```
mkdir myblogs
cd myblogs
```
# Creating a virtual environment 
For better management we have to create a virtual environment in the same myblog directory. we can also create virtual environment anywhere in the system.
```
C:\Users\Name\myblogs> py -m venv env
```
# Working with virtualenv
Start your virtual environment by running
```
C:\Users\Name\myblogs> env\Scripts\activate
```
To deactivate virtual environment by running 
```
(env) C:\Users\Name\myblogs> env\Scripts\deactivate
```
# Installing Django & Other dependencies
I have created a requirement.txt file and the associated Django vertion for this project.
Now run the following command to install Django
```
(env) C:\Users\Name\myblogs> pip install -r requirements.txt
```

