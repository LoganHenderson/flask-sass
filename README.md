# flask-sass
Dumb simple package to compile sass files whenever they are edited in your flask app. This was thrown together for my own project when none of the current open source plug ins worked for me. 

### Benefits compared to the similar packages on the internet
* Only 1 single file `scss.py` which only depends on the Python stdlib.
* Unlike the other flask-scss packges I tried using, this package will utilize the sass binary. Thus, you can utilize the most up to date version of sass, unlike the native python sass compilers which may not be up to date.
* Don't waste time guessing where you need to place your sass/css files. Configure everything by editing 4 path variables in the `scss.py`.

### Install
There are three steps to use this package
1. Make sure you have sass installed in the environment that your app is running. The way I use it is is by downloading it into my docker image as so
```
RUN wget https://github.com/sass/dart-sass/releases/download/1.15.2/dart-sass-1.15.2-linux-x64.tar.gz -O /tmp/out.tar.gz \
	&& tar zxvf /tmp/out.tar.gz -C /tmp/ \
	&& mv /tmp/dart-sass/* /usr/local/bin/. \
  && rm -rf /tmp/*
```
You can see this in the context of a flask docker file [here](https://github.com/LoganHenderson/flask-scss/blob/master/Dockerfile). However, if you are not using docker, just change the SASS_PATH variable (discussed below) to wherever your binary is on your dev machine.

2. Drag `scss.py` into your project

3. Import the package into your app, and then initialize it with your application object
```
from .lib import ScssCompiler (I have the file in /app/app/lib, change accordingly)
ScssCompiler(app)
```
### Configure
There are four variables you must make sure are correct at the top of the scss.py file. Here are the values I have used for my project:
```
SCSS_DIR_PATH = '/app/app/static/scss'
SCSS_FILE_PATH = '/app/app/static/scss/main.scss'
OUTPUT_CSS_FILE_PATH = '/app/app/static/main_new.css'
SASS_PATH = '/usr/local/bin/sass'
```
* SCSS_DIR_PATH: Changes to any file in the dir will trigger a re-compile.
* SCSS_FILE_PATH: When a re-compile is triggered it will compile the scss file here.
* OUTPUT_CSS_FILE_PATH: When a re-compile is triggered it will put the resulting css file here.
* SASS_PATH: Where you are storing the sass executable.
