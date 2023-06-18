import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import database as db
import datetime
import notification

pas='your password' #create App password from your google account 
sender="your email id" #
#---------------------------------------------------------------mail function----------------------------------------------------------------

def send_email(subject, locality, id , user_name, festival):
    # Open the image file and read its contents
    image_path=f"fest_photos\\{id}.jpg"
    with open(image_path, 'rb') as f:
        image_data = f.read()
    _mail=[]
    if locality!="India":
        cus_mail=list(db.connection("select email_id from customers where cust_state=%s",(locality ,)))
        for i in cus_mail:
            _mail.append((i))
    else:
            _mail=list(db.connection("select email_id from customers"))

    print(_mail)
    # Create a multi-part message object and set the subject, from, and to fields
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] =', '.join(str(_mail))

    # Add the HTML body to the email and replace the img src with the Content-ID of the image
    html_body = f"""<html><body><p style="font-size:15px; ">Dear valued customer,</p> 

    <p  style="font-size:14px;" >Wishing you and your loved ones a joyous and prosperous {festival} !
      May this festival bring happiness, good health, and abundance into your life.</p> 

     <p style="font-size:14px;" >On this special occasion, I hope you get to spend quality time with your family and friends, 
     enjoy delicious food, and create unforgettable memories. Make this festival more special with our special offers on our products</p> 

     <p style="font-size:15px;" >Best regards,</p> 
     
     <p style="font-size:15px; font-weight: bold;">{user_name}</p>   <img src="cid:image" style="width:80%;"></body></html>"""
    

    message.attach(MIMEText(html_body, 'html'))
    message_image = MIMEImage(image_data)
    message_image.add_header('Content-ID', '<image>')
    message.attach(message_image)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, pas) # Enter your email password here
        if len(_mail)==1:
            smtp.sendmail(sender, _mail[0], message.as_string()) #checking if _mail has more than one recipient if not checking givig  error

        elif len(_mail)>1:
            smtp.sendmail(sender, _mail, message.as_string())
            
        notification.notify()
        return _mail
#----------------------------------------------------------------end of function send_email----------------------------------------------------------------


 
#----------------------------------------------------------------detecting festival------------------------------------------------------------------------------------
def dec_fest(user):
    id=""
    festival =""
    fdate=""
    locality=""


    dt=datetime.datetime.now()
    date=dt.date()
    result=db.connection("select * from fest_india where fest_date= %s" ,(date,)) 
    if result:
        for i in result:
            id=i[0]
            festival=i[1]   
            fdate=i[2]
            locality=i[3]

        emails=send_email(f"Greetings from {user} ", locality, id , user, festival)
        return festival,emails

    else:
        return festival,0

#----------------------------------------------------------------detecting festival------------------------------------------------------------------------------------

def bday_send_email(subject, recipients ,name ,location ,user, points,image_path="fest_photos\\bday.jpg"):
    # Open the image file and read its contents
    with open(image_path, 'rb') as f:
        image_data = f.read()

    # Create a multi-part message object and set the subject, from, and to fields
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender

    if len(recipients)==1:
        message['To'] =recipients

    elif len(recipients)>1:
        message['To'] =', '.join(recipients)
    if points>10:
    # Add the HTML body to the email and replace the img src with the Content-ID of the image
        html_body = f"""<html><body><p style="font-size:15px " >Dear {name},</p> 

    <p style="font-size:14px ">Happy Birthday {name}! We hope that your day is filled with joy and celebration.</p> 
    <p style="font-size:14px ">We hope that your day is filled with joy and celebration. As a token of our appreciation, we would like to offer you a special birthday discount of 10% on your next purchase with us at our {location.capitalize()} store.</p> 
     
       <p style="font-size:14px">We value your loyalty as a customer and hope that you continue to choose us products and services for all of your needs. </p> 
       <p style="font-size:14px">Thank you for being a part of our community.</p>
       <p style="font-size:14px">Best regards,</p>
       <p style="font-size:14px;  font-weight:bold; ">{user}</p>
        <img src="cid:image" style="width:80%;"></body></html>"""

    else:
        html_body = f"""<html><body><p style="font-size:15px ;" >Dear {name},</p> 

    <p style="font-size:14px;">Happy Birthday {name}! We hope that your day is filled with joy and celebration.</p> 
    <p style="font-size:14px; ">We hope that your day is filled with joy and celebration. make your birthday more joyfull with us at our {location.capitalize()} store.</p> 
       <p style="font-size:14px;">We value your loyalty as a customer and hope that you continue to choose us products and services for all of your needs. </p> 
       <p style="font-size:14px;">Thank you for being a part of our community.</p>
       <p style="font-size:14px;">Best regards,</p>
       <p style="font-size:14px;  font-weight:bold; ">{user}</p>
        <img src="cid:image" style="width:80%;"></body></html>"""


    message.attach(MIMEText(html_body, 'html'))
    message_image = MIMEImage(image_data)
    message_image.add_header('Content-ID', '<image>')
    message.attach(message_image)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(sender, pas) # Enter your email password here
        if len(recipients)==1:
            smtp.sendmail(sender, recipients[0], message.as_string()) #checking if recipients has more than one recipient if not checking givig  error

        elif len(recipients)>1:
            smtp.sendmail(sender, recipients, message.as_string())
            
        notification.notify()


def dec_bday(user):

    id=''
    name=''
    email=''
    location=''
    bday=''
    points=""
    dt=datetime.datetime.now()
    mdate = dt.strftime('%m')
    ddate=dt.strftime('%d')
    result=db.connection("SELECT * from customers where MONTH(birthday) = %s AND DAY(birthday) = %s" ,(mdate,ddate))
    if result:
        for i in result:
            id=i[0]
            name=i[1]
            email=i[2]
            location=i[3]
            points=i[5]

        bday_send_email("Celebrate Your Birthday with a Special Offer", [email,""] ,name ,location, user, points)
        return name
    

    else:
        return name
    
