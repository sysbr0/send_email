import random
import smtplib
import ssl
from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

def generate_verification_code():
    return str(random.randint(100000, 999999))

def send_verification_email():
    email_receiver = email_entry.get()
    global verification_code
    verification_code = generate_verification_code()

    # Email configuration
    email_sender = 'sysbr76@gmail.com'
    email_password = 'exvn tooe pfdb uthz'  # Replace with your Gmail App Password or email password
    subject = 'Verification Code'
    body = f'Your 6-digit verification code is: {verification_code}'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    start_timer()

def verify_email():
    entered_code = code_entry.get()

    if entered_code == verification_code:
        messagebox.showinfo("Success", "Verification Successful!")
    else:
        messagebox.showerror("Error", "Verification Code is incorrect. Please try again.")

def update_timer():
    global remaining_time
    remaining_time -= 1
    timer_label.config(text=f"Time Left: {remaining_time} seconds")
    if remaining_time <= 0:
        timer_label.config(text="Time's Up!")
        verify_button.config(state=DISABLED)
        resend_button.config(state=NORMAL)
    else:
        timer_label.after(1000, update_timer)

def start_timer():
    global remaining_time
    remaining_time = 120
    timer_label.config(text=f"Time Left: {remaining_time} seconds")
    verify_button.config(state=NORMAL)
    resend_button.config(state=DISABLED)
    update_timer()

def resend_verification():
    global verification_code, remaining_time
    verification_code = generate_verification_code()
    start_timer()

root = Tk()
root.title("Email Verification")

email_label = Label(root, text="Enter your email:")
email_entry = Entry(root)
send_button = Button(root, text="Send Verification Code", command=send_verification_email)

code_label = Label(root, text="Enter the verification code:")
code_entry = Entry(root)
verify_button = Button(root, text="Verify", command=verify_email)
resend_button = Button(root, text="Resend Code", command=resend_verification)

timer_label = Label(root, text="Time Left: 120 seconds")

email_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
email_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
send_button.grid(row=1, column=0, columnspan=3, pady=10)

code_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
code_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
verify_button.grid(row=3, column=0, columnspan=3, pady=10)
resend_button.grid(row=4, column=0, columnspan=3, pady=10)

timer_label.grid(row=5, column=0, columnspan=3, pady=10)

verification_code = ""
remaining_time = 120

root.mainloop()
