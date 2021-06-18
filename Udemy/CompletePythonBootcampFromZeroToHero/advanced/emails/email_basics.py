# (control + '/' for comments)


##################################################################
# PROVIDER                      SMTP server domain name
# Gmail                         smtp.gmail.com
# Yahoo Mail                    smtp.mail.yahoo.com
# Outlook.com/Hotmail.com       smtp-mail.outlook.com
# Other US emails (ignored)

##################################################################


##################################################################
# Sending emails
##################################################################
import smtplib

gmail_smtp_server = 'smtp.gmail.com'
port_no_1 = 587  #TLS encryption
port_no_2 = 465
smtp_object = smtplib.SMTP(gmail_smtp_server,port_no_1)
smtp_object.ehlo()  #### MUST RUN THIS IMMEDIATELY AFTER GETTING THE OBJECT ###
smtp_object.starttls() # For port_no_1 - 587 (Can skip this step if using port 465)


##################################################################
# Setup sending email to GMAIL
# First Login and Go to Google Accounts Page - myaccount.google.com
# Go to Security Tab
# Turn on 2-step verification (No need this step if already turned on)
# Go back to Security Tab
# Go into App passwords 
# Under "Select the app and device you want to generate the app password for.",
# for "Select App", select "Mail"
# for "Select Device", select "Other (Custom Name)" and use whatever name you want to call it
# A password will be generated
# Save that password somewhere
##################################################################


##################################################################
# SEND EMAIL TO GMAIL - UNCOMMENT TO SEND EMAILS
##################################################################
import getpass #type:ignore  # Same as input("Message"), except non visible
email = "leonghuiwen@gmail.com" #input("Email: ")
password = "lmihyrtrxxfqwxow" #getpass.getpass("Password: ")  #Enter that generated password/ if forgotten, then go generate one more
# smtp_object.login(email,password)

# from_address = email
# to_address = email
# subject = input("Subject: ")
# message = input("Message: ")
# msg = "Subject: "+subject+"\n"+message

# # Now to send email
# smtp_object.sendmail(from_address,to_address,msg)
# smtp_object.quit()
# print("Message sent. ")



##################################################################
# READ EMAIL TO GMAIL
#
# Keywords:
# BEFORE date
# ON date
# SINCE date
# FROM some_string
# TO some_string
# CC some_string
# SUBJECT string
# BODY string
# TEXT string with spaces
# SEEN / UNSEEN
# ANSWERED / UNANSWERED
# DELETED / UNDELETED
##################################################################

import imaplib
imap_object = imaplib.IMAP4_SSL('imap.gmail.com')
imap_object.login(email,password)
#print(imap_object.list())

imap_object.select('inbox')

search_criteria = 'SUBJECT "HEYA"'
typ, data = imap_object.search(None,search_criteria)
email_id = data[0]

print(f"Retrieving message with search criteria: {search_criteria}")
result, email_data = imap_object.fetch(email_id,'(RFC822)')  #'(RFC822)' is a protocol. no idea what it is for yet
raw_email = email_data[0][1].decode('utf-8') #type:ignore
print(raw_email) #type:ignore

import email
plain_text = 'text/plain'
link_text = 'text/html'

email_message = email.message_from_string(raw_email) #type:ignore
for e in email_message.walk():
    if e.get_content_type() == plain_text:
        body = e.get_payload(decode=True)
        print(f"== {body}")