from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, timedelta
import time
from email.message import EmailMessage
import smtplib
import keyring

carList = ['', 'Accord 2018', 'Audi S4', 'Minivan']
print("Welcome to Amoshet's Permit Parking Script!")
print("Which car would you like to register for street parking?")

#prints list of cars
for i in range(1, len(carList)):
	print(str(i) + ". " + carList[i])

addNew = len(carList)
print(str(addNew) + ". Add Car")

#asks user to select car
car = int(input("Please select car by number: "))

addr = "244 Prospect Avenue"
#changes car, car color, and license plate based on number selected
if (car == carList.index('Accord 2018')):
	car = "Honda Accord 2018"
	carColor = "Red"
	licensePlate = "X2B43C"
	num = '2015953342'
	email = "opdparkingpermit@gmail.com"
	
if (car == carList.index('Audi S4')):
	car = "Audi S4 2013"
	carColor = "Grey"
	licensePlate = "JRE493"
	num = '2019823220'
	email = "opdparkingpermit@gmail.com"

if (car == carList.index('Minivan')):
	car = "Toyota Sienna 2022"
	carColor = "White"
	licensePlate = "W33CDR"
	num = '2019823220'
	email = "opdparkingpermit@gmail.com"

if (car == addNew):
	car = input("What is your car's Make and Model? (Ex: Toyota Corolla): ")
	carColor = input("What color is your car? (Ex: Red): " )
	licensePlate = input("And what is your license plate? (Ex: LBJ3M7): " )
	num = input("What phone number can you be reached at? (Ex: 2019875220:")

#TODO Add check that time isn't past midnight. If it is, subtract 1 for the day.
#gets date from system and splits it for the input fields
t = date.today()
date = t.strftime("%m/%d/%Y")
dateSplit = date.split('/')
#todays date split for the form
d1 = dateSplit[0]
d2 = dateSplit[1]
d3 = dateSplit[2]

#tomorrows date
t2 = t + timedelta(days=1)
date2 = t2.strftime("%m/%d/%Y")
dateSplit2 = date2.split('/')
d4 = dateSplit2[0]
d5 = dateSplit2[1]
d6 = dateSplit2[2]

#sets options to disable random error(s)
options = webdriver.ChromeOptions()
#options.add_experimental_option("excludeSwitches", ["enable-logging"])
#starts browser, we changed this to a remote webdriver
browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)  # webdriver.Chrome(options=options)
browser.get('https://www.oradellpolice.com/overnight-parking-2')


#locates and fills form with user number
input_num = browser.find_element(By.CLASS_NAME, "LUo2uiVuzd_8DPcbkxNw")
input_num.send_keys(num)

#sets list
info = [addr, car, carColor, licensePlate]
elem = browser.find_elements(By.CLASS_NAME, "exokPtqDa3qLy42TT3gA")
#iterates through input fields and fills them, the -2 is because the date fields also use this class name
#but are being processed differently
for i in range((len(elem)-2)):
	elem[i].send_keys(info[i])

#creates list for date 1 and date 2 and then fills into the form
date_info = [d1, d2, d3, d4, d5, d6]
input_date = browser.find_elements(By.CLASS_NAME, "Bg_YtgRmubEGz0lAljF9")
#iterates through input fields and fills them
for i in range(len(elem)):
	if i < 3: #populates the first date
		input_date[0].send_keys(date_info[i])
	else:     #populates the second date
		input_date[1].send_keys(date_info[i])


#submits form after 3 seconds and closes page
time.sleep(3)
#submitForm = browser.find_element(By.CLASS_NAME, "button")
#submitForm.click()
print("submit button during debugging")
time.sleep(3)
browser.quit()

'''
#s = smtplib.SMTP('smtp.gmail.com', 587)
server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
# start TLS for security 
server.starttls()
  
# Authentication 
server.login("opdparkingpermit@gmail.com", keyring.get_password("email", "opd"))
#s.login("opdparkingpermit@gmail.com", keyring.get_password("email", "opd"))

# message to be sent
message = "Your " + car + " has been successfully registered for overnight parking on " + date + " and " + date2 + ". Thank you for using our service!"
msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = "Overnight Parking Request"
msg['From'] = "opdparkingpermit@gmail.com"
msg['To'] = email
server.send_message(msg)
server.quit()

# sending the mail 
server.sendmail("opdparkingpermit@gmail.com", email, message)

# terminating the session 
server.quit()
'''