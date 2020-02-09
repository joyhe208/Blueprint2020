import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "kalyan.conrado@eellee.org"
receiver_email = "kalyan.conrado@eellee.org"
password = "robertisbob"
message = "What is good?"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)