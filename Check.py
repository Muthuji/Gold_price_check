import smtplib
import pricecheck
from python_whatsapp_bot import Whatsapp
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

Token='874317060671237|JiPZzDGezmtM0oehEbzgQ2ux-vU'
wa_bot = Whatsapp(number_id='8072407662' ,token=Token)
wa_bot.send_message('mobile eg: 2348145xxxxx3', 'Your message here')
