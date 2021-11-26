import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
username='bimsnepalcalcgen@gmail.com'
password='shrestha123'

def send_mail(to_emails,text='Email Body',subject='Interest Shown',
 from_email       ='BIMS Nepal <bimsnepalcalcgen@gmail.com>'):
    assert isinstance(to_emails,list)
    msg           =MIMEMultipart('alternative')
    msg['From']   =from_email
    msg['To']     =",".join(to_emails)
    msg['Subject']=subject
    
    txt_part      =MIMEText(text,'plain')
    msg.attach(txt_part)

    msg_str       =msg.as_string()
    #nowl ogin to smtp server
    server        =smtplib.SMTP(host='smtp.gmail.com',port=587)   
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email,to_emails,msg_str)

    server.quit()
