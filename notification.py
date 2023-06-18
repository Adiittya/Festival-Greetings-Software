import time
from winotify import Notification ,audio

def notify(message="Mail sent",icon='fest_photos\\20.jpg'):

    toast = Notification(app_id='Adi script',   #name of the notification
                        title='Message title',  #title of the notification
                        msg=message,  #msg of the notification
                        duration='short',  #duration of the message
                        icon=icon)  #icon of the notification

    toast.set_audio(audio.Reminder, loop=False)  #set the audio
    toast.add_actions(label="click here", launch='https://mail.google.com/mail/u/0/#inbox')  #set the button to launch something
    toast.show()  #show the notification