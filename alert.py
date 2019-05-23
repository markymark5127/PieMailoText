import smtplib

smtpUser = 'Youremail@gmail'
smtpPass = 'yourapppassword'

toAdd = 'phonenumber@txt.att.net'
toAdd2 = 'phonenumber@vtext.com'
fromAdd = smtpUser

subject = 'Baby Monitor Alert'

header = "To: " + toAdd + '\n' + 'To: '+ toAdd2 + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'Zoie\'s Awake!\nApp: ipcamviewer://launch \nWeb: http://ipaddress/html/min.php'

header2 = "To: " + toAdd2 + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject


print header + '\n' + body

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n' + body)
s.sendmail(fromAdd, toAdd2, header2 + '\n' + body)
s.quit()
