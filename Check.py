import smtplib
import pricecheck
# creates SMTP session

s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
sender='hapieeji@gmail.com'
rec='usermuthukumaran@gmail.com'
passs='lrgdsubqbjcqybmo'
# Authentication

s.login(sender, passs)
 
# message to be sent

message = "Message_you_need_to_send"
 
# sending the mail

s.sendmail(sender, rec, pricecheck.ans)
 
# terminating the session
s.quit()