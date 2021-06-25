import time
import smtplib
import pyautogui as pg
import webbrowser as web
from urllib.parse import quote

def sendMail(mailFrom, mailFromPass, mailTo, contents):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(mailFrom, mailFromPass)
    server.sendmail(mailFrom, mailTo, contents)
    server.close()
def sendwhatmsg(phone_no, message):
    parsedMessage = quote(message)
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage)
    time.sleep(2)
    width,height = pg.size()
    pg.click(width/2,height/2)
    time.sleep(10)
    pg.press('enter')

#sendMail(mailFrom, mailFromPass, mailTo, contents)
#sendwhatmsg(phone_no, message)
