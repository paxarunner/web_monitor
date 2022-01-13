import os
import smtplib
import requests
import logging
import ctypes

EMAIL_ADDRESS = 'login@domain.com'
EMAIL_PASSWORD = 'password' 

pk = 'http://192.168.42.115:8080'
pz = 'http://192.168.43.106:8085'
pv = 'http://192.168.40.104:8085'
mk = 'http://192.168.42.24:9000'

logging.basicConfig(filename=r'C:\bin\monik.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def notify_user():
    global system
    mbox(f'{system} not responding', "       TBD application", 1)
    with smtplib.SMTP('smtp.ya.ru', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f'{system} not responding!'
        body = 'Do something for resovle!'
        msg = f'Subject: {subject}\n\n{body}'
        logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, 'ktk@rcompany.kz', msg)
def mbox(text, title, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

try:
    for sys in (pk, pz, pv, mk):
        system = sys                         #Здесь присваиваем system
        r = requests.get(sys, timeout=3)
        logging.info(f'{system} is UP')

except Exception as e:   
    logging.info(f'{system} is DOWN!')
    notify_user()
