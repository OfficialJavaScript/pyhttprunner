# pyhttprunner
Basic alternative to Python's http.server built in Flask.

# Setup

To get started you need to have Python 3 installed (Preferably the latest.)

Now you need to install the requirements:

```pip3 install -r requirements.txt```

Now you need to move your website files to the /website folder.

In your scripts if you have any static files (such as images, scripts or styles), you will need to change the address to /static/path/to/file.

For example:

Before:

```<link rel="stylesheet" href="/style/style.css">```

```<link rel="icon" href="/images/logo.png" type="image/x-icon">```

After:

```<link rel="stylesheet" href="/static/style/style.css">```

```<link rel="icon" href="/static/images/logo.png" type="image/x-icon">```

If you have done all the steps correctly, you should be able to run ```python3 main.py``` 

You can then access the site from:

```http://localhost/```

```localhost```

```127.0.0.1```

The port number by default is 80, if you wish you change this on line 27:

```app.run('0.0.0.0', port=80)```

Change the line ```port=80``` to whatever port you want, ```port=8080```
