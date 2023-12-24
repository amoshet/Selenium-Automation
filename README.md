# Selenium-Automation
Web Automation Project that fills out an overnight parking request form for the user using Docker and Selenium with Python 3.9

Software Needed:
Docker

Steps to setup container on Windows:

1) Open terminal session in the Selenium-Automation folder.

#this will pull selenium grid with 2 chrome nodes (multicontainer), as well as a mysql and phpmyadmin container. It also maps port 7900 and 7901 for noVNC, which allows you to see what is happening on the chrome containers. Mysql is mapped to port 3306 and phpmyadmin is mapped to port 8080 on host.

2) Run command "docker compose up -d"

![container](https://i.imgur.com/1GUFqcC.png)

Run the automation script:

1) In your terminal, run command "python autopark.py"

2) Follow script instructions and input a number to permit park your car! If you select Add Car, you will be
asked to input your information before the script runs and autocompletes your form. This information is sent to a db carsDB and is saved on a persistent volume. You can run two concurrent sessions and register two different cars at the same time, as two containers are setup for this script.

![Autopark.py](https://i.imgur.com/6AYQKNr.png)

3) (optional) open your web browser and go to "http://localhost:7900/?autoconnect=1&resize=scale&password=secret" #this allows you to view what is happening on the container when you run the script

![site](https://i.imgur.com/dHSYaS4.png)

#this shows the grid with multiple sessions running in selenium grid (multiple containers running at the same time)

![grid](https://i.imgur.com/gHdPpDT.png)
