# pyhttprunner
Basic alternative to Python's http.server built in Flask.

# Setup
<details>
<summary>Step 0.5</summary>

<br>
To get started you need to have Python 3 installed (Preferably the latest.)
</details>
<details>
<summary>Step 1</summary>

<br>
Now you need to install the requirements:

```pip3 install -r requirements.txt```
</details>
<details>
<summary>Step 2</summary>

<br>
Now you need to move your website files to the /website folder.
</details>
<details>
<summary>Step 3</summary>

<br>
In your scripts if you have any static files (such as images, scripts or styles), you will need to change the address to /static/path/to/file.

<br>
<details>
<summary>Example</summary>
  
Before:
  
```<link rel="stylesheet" href="/style/style.css">```

```<link rel="icon" href="/images/logo.png" type="image/x-icon">```

After:

```<link rel="stylesheet" href="/static/style/style.css">```

```<link rel="icon" href="/static/images/logo.png" type="image/x-icon">```

</details>
</details>
<br>

If you have done all the steps correctly, you should be able to run ```python3 main.py``` 

## Access Site

You can then access the site from:

```http://localhost/```

```localhost```

```http://127.0.0.1/```

```http://127.0.0.1/:80```

## Change port

The port number by default is 80, if you wish you change this on line 27:

```app.run('0.0.0.0', port=80)```

Change the line ```port=80``` to whatever port you want, ```port=8080```

## Access from other devices

In the output, you can see what address the program is running on:

```
* Running on http://127.0.0.1:80
* Running on http://192.168.1.28:80
```

In the second line, we see the local IP the program is running on, on another device (on the same network) you can go to this address to access the website.
