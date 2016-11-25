import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


html = """\
        <html>
        <head></head>
        <body>
            <p>Hi!<br>
            How are you?<br>
            Your ticket was generated successfully.
            </p>
        </body>
        </html>
        """

 
def send_email(reciepient, table):

    fromaddr = "eventwiser@gmail.com"
    toaddr = reciepient
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Awesome Eventwiser"
    # print(table)
    body = "It Looks like you will be attending event: '%s' at '%s'" % (table[0], table[1])
    
    msg.attach(MIMEText(html, 'html'))
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "spongebobandbravo")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# send the ticket.
def send_ticket(reciepient, table):

    fromaddr = "eventwiser@gmail.com"
    toaddr = reciepient
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Get Your Ticket"
    # print(table)
    body = "Your Ticket is: '%s' and looks like it is '%s'" % (table[0], table[1])

    msg.attach(MIMEText(html, 'html'))
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "spongebobandbravo")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()








