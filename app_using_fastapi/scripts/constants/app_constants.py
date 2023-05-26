"""
This constant page is for calling the api names
"""
import os


class CommonConstants:
    STUDENT_ENDPOINT = "/students/"
    STUDENT_ID_ENDPOINT = "/students/id"
    STUDENT_ID_COURSES_ENDPOINT = "/students/{id}{courses}"
    STUDENT_NAME_ENDPOINT = "/students/{name}"
    STUDENT_ADD_ENDPOINT = "/students/course/"
    STUDENT_FIND_ENDPOINT = "/students/find"
    EMAIL_ENDPOINT = "/mail"
    AGGREGATE_ENDPOINT = "/aggregate"

class Email_constants:
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('MAIL_ID')
    smtp_password = os.getenv('MAIL_PASSWORD')
    #print(smtp_username, smtp_password)

    # Set up the email content and recipient
    sender_email = 'serinsvarghese@gmail.com'
    subject = 'Data Email'
