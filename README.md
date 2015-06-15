# android-passwd-creator
A simple script that parses the packages.xml file of the Android system and creates a fair version of the corresponding Linux passwd file. In addition, it uses some predefined Master Android UIDs.

This shouldn't be much of a use to you, but I wrote it because I wanted to do some Android forensics with Sleuth Kit's mactime tool, so its results look better if you feed it with a "passwd" file which maps some of the Android's UIDs to names.

In order to use it, simply pull the packages.xml file from your android device with ADB (or any other way) and feed it to the script. 

optional arguments:

  -h, --help  show this help message and exit

  -i [I]      Packages.xml file's path.

  -o [O]      Output destination path of passwd file produced.
