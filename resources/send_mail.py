# Copyright (C) Woofy, Inc. - All Rights Reserved
# Unauthorized copying of this file, via any medium, is strictly prohibited
# Proprietary and confidential
# Author: Arjun Rai, arjun@hellowoofy.com, December 2019

import smtplib
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

from datetime import datetime
import time

import json
import os

import falcon


class SendReport:

    def __init__(self):
        pass

    @staticmethod
    def send_mail(student_info, to_email):
        # me == my email address
        # you == recipient's email address
        from_email = "arun.g.ghontale@gmail.com"

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Student Report for {}".format(student_info["student_name"])

        msg['From'] = from_email
        msg['To'] = to_email

        # Create the body of the message (a plain-text and an HTML version).
        table_html = ''

        attendance_reports = student_info["attendance_report"]
        for attendance_report in attendance_reports:
            table_html += '<tr>'
            table_html += '<td>' + str(attendance_report["class"]) + '</td>'
            table_html += '<td>' + str(attendance_report["percentage"]) + '</td>'
            table_html += '<td>' + str(attendance_report["classes_attended"]) + '</td>'
            table_html += '</tr>'

        html = """\
    <html>
      <head>
        <style> 
            {style}
        </style>
      </head>
      <body>
        <table class="table1">
            <thead>
            <th>Class</th>
            <th>Attendance Percentage</th>
            <th>Classes Attended</th>
            </thead>
        {table_code}
        </table>
      </body>
    </html>
    """.format(table_code=table_html,
               style='.table1, .table1 td, .table1 th { border: 1px solid black; border-collapse'
                     ': collapse; text-align:center; white-space: nowrap;}')

        # Record the MIME types of both parts - text/plain and text/html.
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        msg.attach(part2)

        # Send the message via local SMTP server.
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(from_email, "qcbjezokoxeiyxmt")
        # sendmail function takes 3 arguments: sender's address, recipient's address
        # and message to send - here it is sent as one string.
        s.sendmail(from_email, to_email, msg.as_string())
        print('Email sent for:', datetime.now().date())
        s.quit()

    def on_get(self, req, resp):
        # TODO - to be replaced by sending mail from dynamic report
        t1 = threading.Thread(target=send_student_report, args=())
        t1.start()

        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_HTML

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.content_type = falcon.MEDIA_HTML


def send_student_report():
    students = [
        {
            "student_info": {
                "student_name": "Aditya Ghontale",
                "attendance_report": [{
                    "class": "Java",
                    "percentage": "80%",
                    "classes_attended": "4/5"
                }, {
                    "class": "Node",
                    "percentage": "50%",
                    "classes_attended": "3/6"
                }]
            },
            "to_email": "arun.g.ghontale@gmail.com"
        },
        {
            "student_info": {
                "student_name": "Arun Ghontale",
                "attendance_report": [{
                    "class": "Java",
                    "percentage": "100%",
                    "classes_attended": "5/5"
                }, {
                    "class": "Node",
                    "percentage": "33.33%",
                    "classes_attended": "2/6"
                }]
            },
            "to_email": "arun.g.ghontale@gmail.com"
        }
    ]
    for student in students:
        SendReport.send_mail(student_info=student["student_info"], to_email=student["to_email"])


if __name__ == '__main__':
    send_student_report()
