import sqlite3 
from sqlite3 import Error 
import syslog
import json
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class User:
    def Registeruser(self,uname,password,email):
        con=sqlite3.connect('sqlbd.db')
        sql="insert into user value ('{0}','{1}','{2}')".format(uname,password,email)
        con.execute(sql)
        con.commit()
        print(f"user is successfullty register with {uname} with {password}")


class Logger:
    def LogError(self,msg):
        syslog.syslog(syslog.LOG_EPP,msg)

class Email:
    def Sendmail(self,to_email,message_content,subject='user registered'):
        with open('cred.json') as f:
            data = json.load(f)
        smtp_server="smtp.gamil.com"
        port=465
        sender_mail=data["usermail"]
        password=data["passw"]
        context=ssl.create_default_context()
        message=MIMEMultipart('alternative')
        message["From"]=sender_mail
        message['To']=subject
        message_content= f'Hello,<br/><b>Message from kaashish </b><br/>
        {message_content}<br/> all the best,<br/>'
        part=MIMEText(message_content,"html")
        message.attach(part)
        with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
            server.login(sender_mail,password)
            server.sendmail(sender_mail,to_email,message.as_string())
    
        print(f"mail send to {to_email}") 


class Register:
    def Registeruser(self,uname,pwd,email):
        try:
            User().Registeruser(uname,pwd,email)
            Email().Sendmail(email,'You have succesfully resgister')

        except Exception:
            Logger().WriteLogToSystem('something wrong')


obj=Register()
obj.Registeruser('kashish','lajibolala','kashishhsinghhh@gmail.com')

