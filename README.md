# Selenium-Automation
Web Automation Project that fills out an overnight parking request form for the user using Docker and Selenium with Python 3.9

Software Needed:
Docker

Steps to setup container on Windows:

1) Open terminal session in the Selenium-Automation folder.

#this will pull the selenium standalone image if needed and run it on port 4444 on your browser in detached mode with 2GB of memory. It also maps port 7900 for noVNC, which allows you to see what is happening on the container

2) Run command "docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:4.16.1-20231212" 

#this allows you to view what is happening on the container when you run the script

3) (optional) open your web browser and go to "http://localhost:7900/?autoconnect=1&resize=scale&password=secret" 

Run the automation script:

1) In your terminal, run command "python autopark.py"

2) Follow script instructions and input a number to permit park your car! If you select Add Car, you will be
asked to input your information before the script runs and autocompletes your form.

Features Coming Soon:

1) Database functionality so the script can remember your car!
2) SMTP server integration so that confirmation emails can be sent when the form is submitted
3) The ability to run multiple sessions at the same time
