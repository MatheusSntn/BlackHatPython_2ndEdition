import smtplib
from private_credentials import senha, email
import time
import win32com.client

smtp_server = 'smtp.office365.com'
smtp_port = 587
smtp_acct = str(email)
smtp_password = str(senha)
tgt_accts = [f'{email}']

def plain_email(subject, contents):
    message = f'Subject: {subject}\nFrom {smtp_acct}\n'
    message += f'To: {tgt_accts}\n {contents}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    server.login(smtp_acct, smtp_password)

    server.sendmail(smtp_acct, tgt_accts, message)
    time.sleep(1)
    server.quit()

if __name__ == '__main__':
    plain_email('test2 message', 'attack at dawn.')
