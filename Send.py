import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import csv

while True:

	with open('Emails.csv','r') as f:
	    reader = csv.reader(f)
	    for row in reader:
		email_user = '@'# replace the @ with your email
		email_password = '$'# replace the $ with your email
		email_send = row[0]

		subject = 'My CV'

		msg = MIMEMultipart()
		msg['From'] = email_user
		msg['To'] = email_send
		msg['Subject'] = subject

		body =  'Dears\n,I am sending this email from Python!\nBest regards'
		msg.attach(MIMEText(body,'plain'))

		filename='filename.pdf'
		attachment  =open(filename,'rb')

		part = MIMEBase('application','octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition',"attachment; filename= "+filename)

		msg.attach(part)
		text = msg.as_string()
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(email_user,email_password)
		server.sendmail(email_user,email_send,text)

	server.quit()
	time.sleep(5)
#2021
