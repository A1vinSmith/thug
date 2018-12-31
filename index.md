The number of client-side attacks has grown significantly in the past few years shifting focus on poorly protected vulnerable clients. Just as the most known honeypot technologies enable research into server-side attacks, honeyclients allow the study of client-side attacks. A complement to honeypots, a honeyclient is a tool designed to mimic the behavior of a user-driven network client application, such as a web browser, and be exploited by an attacker’s content.

Requirements
============

- Python 2.7
	http://www.python.org/

- Google V8
	http://code.google.com/p/v8/

- PyV8
	http://code.google.com/p/pyv8/

- Beautiful Soup 4
	http://www.crummy.com/software/BeautifulSoup/

- Libemu
	http://libemu.carnivore.it/

- Pylibemu
	https://github.com/buffer/pylibemu

- Pefile
	http://code.google.com/p/pefile/

- Chardet
	http://chardet.feedparser.org/

- httplib2 0.7.1 or later
	http://code.google.com/p/httplib2/

- MongoDB (optional)
	http://www.mongodb.org/

- PyMongo (optional)
	http://www.mongodb.org/display/DOCS/Python+Language+Center


Installation
============

- BeautifulSoup 4

Currently the best way to install Beautiful Soup 4 is through `easy_install'
because it is still in beta release. Beautiful Soup 4 is published through 
PyPi, so you can install it with easy_install or pip. The package name is 
beautifulsoup4, and the same package works on Python 2 and Python 3.

	# easy_install beautifulsoup4  

or alternatively

	# pip install beautifulsoup4
 

- V8/PyV8

In order to properly install V8 and PyV8 please follow the procedure
described below.


1. Checkout V8 source code from SVN  

        $ svn checkout http://v8.googlecode.com/svn/trunk/ v8

2. Patch V8 source code with the patches you can find in thug/patches
   directory

        $ cp thug/patches/V8-patch* .
        $ patch -p0 < V8-patch1.diff 
        patching file v8/src/log.h
        $ patch -p0 < V8-patch2.diff 
        patching file v8/src/parser.h
        Hunk #1 succeeded at 456 (offset 7 lines).

3. Checkout PyV8 source code from SVN

        $ svn checkout http://pyv8.googlecode.com/svn/trunk/ pyv8

4. Set the environment variable V8_HOME with the V8 source code 
   absolute path (you need to change the value reported below)

        $ export V8_HOME=/home/buffer/v8

5. Move to PyV8 source code directory

        $ cd pyv8

6. Build and install (PyV8 setup.py will properly install both V8
   and PyV8)

        ~/pyv8 $ python setup.py build
        ~/pyv8 $ sudo python setup.py install

7. Test the installation

        ~/pyv8 $ python PyV8.py

   If no problems occur, you have successfully installed V8 and PyV8.


In order to install the other required libraries and packages please 
follow installation procedures as specified in their documentation.


Usage
=====


    ~/thug/src $ python thug.py -h

        Synopsis:
        Thug: Pure Python honeyclient implementation

        Usage:
            python thug.py [ options ] url

        Options:
            -h, --help          	Display this help information
            -u, --useragent=    
            -o, --output=       	Log to a specified file
            -l, --local         
            -v, --verbose       	Enable verbose mode    
            -d, --debug         	Enable debug mode

        Available User-Agents:
	    xpie60			Internet Explorer 6.0 (Windows XP)
	    xpie61			Internet Explorer 6.1 (Windows XP)
	    xpie70			Internet Explorer 7.0 (Windows XP)
	    xpie80			Internet Explorer 8.0 (Windows XP)
	    w2kie60			Internet Explorer 6.0 (Windows 2000)
	    w2kie80			Internet Explorer 8.0 (Windows 2000)

Please note that Thug store downloaded contents and logs in the directory 
thug/logs by default if not otherwise specified. You are required to take 
a look at thug/logs/thug.csv file in order to understand in which directory
logs were saved. This awful logging mechanism will change soon. Moreover it 
is highly suggested to always specify a log file (through option -o).


License information
===================

Copyright (C) 2011-2012 Angelo Dell'Aera

License: GNU General Public License, version 2 or later; see COPYING.txt
         included in this archive for details.


