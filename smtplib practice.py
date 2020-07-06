import smtplib
from email.message import EmailMessage
import imghdr

msg = EmailMessage()

msg['Subject'] = 'Check this out'
msg['From'] = 'gali9600@gmail.com'
msg['To'] = 'ggalina@copaair.com'
msg.set_content('Image attached...')

with open('comic.png','rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='application',subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('gali9600@gmail.com','iidtivycuphdtkay')
    #se usa el correo y el app password generado por google

    smtp.send_message(msg)  

    
