# Little Snakey

### The Cross OS Urban Terror Server Monitor

##### Stand Alone Binaries

OS X - <a href="https://copy.com/P3Z4WfuJ3SRnW1iU">https://copy.com/P3Z4WfuJ3SRnW1iU</a>


##### Manual Installation

The latest version of the software might not be available as stand alone binary for your operating system yet. In that case we recommend that you install it manually. The application was built on top of PySide and Python so you have to install them manually to use the software. Don't be scared, it's quite easy in fact!


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
    
    
###### Other Distros - 

You can find PySide installation guides for all major Linux Distros here - <a href="http://qt-project.org/wiki/PySide_Binaries_Linux">http://qt-project.org/wiki/PySide_Binaries_Linux</a>
    
    
### Issues? Bug Reports? 

Report them here - <a href="https://github.com/urtbd/little-snakey/issues">https://github.com/urtbd/little-snakey/issues</a> 

