import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()

smtp_object.starttls()
password = getpass.getpass()

