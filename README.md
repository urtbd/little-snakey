# Little Snakey

### The Cross OS Urban Terror Server Monitor



##### Installation

The application was built on top of PySide and Python. We're working on building stand alone binaries but until we release those, you have to install the dependencies manually to use it. Don't be scared, it's quite easy in fact!


##### Windows 

(1) Install Python - <a href="http://www.python.org/ftp/python/2.7/python-2.7.msi">http://www.python.org/ftp/python/2.7/python-2.7.msi</a>

(2) Install PySide - <a href="http://releases.qt-project.org/pyside/PySide-1.1.2.win32-py2.7.exe">http://releases.qt-project.org/pyside/PySide-1.1.2.win32-py2.7.exe</a> 

(3) Go to `src` directory and double click `main.py`


#### OS X

(1) It's better to do a separate Python installation using homebrew if you haven't done already - 

    $ brew install python
    
(2) Install PySide using Homebrew -

    $ brew install pyside
    
(3) Please make sure that the brew installed Python is in your system PATH. Add something like these to your bash/zsh profile: 
      
    #Homebrew Python
    export PATH=/usr/local/share/python:$PATH
    
(4) Now you can just run: 

    $ ./run
    
The application should run!

(If you use another package installer for OS X like macports or fink, I have strong belief that you know what to do)


#### Linux 

###### Ubuntu - 

(1) Python comes built in. 
(2) Install Pyside:
    
    $ sudo apt-get install python-pyside
(3) Run:
   
    $ ./run
    
    
### Issues? Bug Reports? 

Report them here - <a href="https://github.com/urtbd/little-snakey/issues">https://github.com/urtbd/little-snakey/issues</a> 

