import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor SMTP
smtp_server = 'mail.modware.lat'
smtp_port = 25
smtp_user = ''  # No necesitas usuario si no has configurado autenticación
smtp_password = ''  # No necesitas contraseña si no has configurado autenticación

# Crear el mensaje
msg = MIMEMultipart()
msg['From'] = 'contacto@modware.lat'
msg['To'] = 'paulmrg461@gmail.com'
msg['Subject'] = 'Test from SMTP'

body = 'This is a test email.'
msg.attach(MIMEText(body, 'plain'))

print(msg.as_string())

# Enviar el correo
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("Correo enviado con éxito")
except Exception as e:
    print(f"Error al enviar el correo: {e}")