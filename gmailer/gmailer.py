#!/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import argparse
import os
import sys

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

def send_email(user, pwd, recipient, subject, body, attaches, reply_to = None, use_ssl = True, use_html = False):
    gmail_user = user
    gmail_pwd = pwd

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = COMMASPACE.join(recipient)
    msg['Date'] = formatdate(localtime = True)
    msg['Subject'] = subject
    if reply_to is not None:
        msg['Reply-to'] = reply_to

    if use_html:
        msg.attach(MIMEText(body, 'html'))
    else:
        msg.attach(MIMEText(body, 'plain'))

    for fname in attaches or []:
        with open(fname, "rb") as f:
            part = MIMEApplication(f.read(), Name = os.path.basename(fname))
            part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(fname)
            msg.attach(part)

    try:
        if use_ssl:
            server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server_ssl.login(gmail_user, gmail_pwd)
            server_ssl.sendmail(user, recipient, msg.as_string())
            server_ssl.close()
        else:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(user, recipient, msg.as_string())
            server.close()
    except Exception as e:
        sys.stderr.write('error: %s\n' % (str(e)))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'command line tool to send email via gmail')
    parser.add_argument('body_file', metavar = 'BODY_FILE', nargs = '?', action = 'store', default = None, help = 'the file to open and send out, \'-\' to read from stdin')
    parser.add_argument('--to', '-t', dest = 'recipient', nargs = '+', action = 'store', default = None, help = 'the recipient to receive email')
    parser.add_argument('--reply-to', '-r', dest = 'reply_to', nargs = '?', action = 'store', default = None, help = 'default reply email address')
    parser.add_argument('--subject', '-s', dest = 'subject', nargs = '?', action = 'store', default = None, help = 'email subject')
    parser.add_argument('--body', '-b', dest = 'body', nargs = '?', action = 'store', default = None, help = 'the message body to send out')
    parser.add_argument('--html', '-m', dest = 'use_html', action = 'store_const', const = True, default = False, help = 'send message body as html')
    parser.add_argument('--attach', '-a', dest = 'attach', nargs = '*', action = 'store', default = None, help = 'files to be attached')
    parser.add_argument('--user', '-u', dest = 'user', nargs = '?', action = 'store', default = None, help = 'gmail user to send email, default read from environment variable GMAILER_USER')
    parser.add_argument('--password', '-p', dest = 'password', nargs = '?', action = 'store', default = None, help = 'gmail user password to authenticate, default read from environment variable GMAILER_PASS')
    parser.add_argument('--ssl', '-l', dest = 'use_ssl', action = 'store_const', const = True, default = False, help = 'send email via SSL')

    args = parser.parse_args()

    if args.user is None:
        try:
            args.user = os.environ['GMAILER_USER']
        except KeyError:
            print 'gmail user not specified or GMAILER_USER is not set'
            exit(1)
    if args.password is None:
        try:
            args.password = os.environ['GMAILER_PASS']
        except KeyError:
            print 'gmail user not specified or GMAILER_PASS is not set'
            exit(1)

    if args.recipient is None or args.subject is None:
        parser.print_help()
    else:
        if args.body_file is not None:
            if args.body_file == '-':
                args.body = ''.join(sys.stdin.readlines())
            else:
                with open(args.body_file, 'r') as f:
                    args.body = f.read()
        elif args.body is None:
            print 'message body not speficied'
            exit(1)

        send_email(args.user, args.password, args.recipient, args.subject, args.body, args.attach, reply_to = args.reply_to, use_ssl = args.use_ssl, use_html = args.use_html)
