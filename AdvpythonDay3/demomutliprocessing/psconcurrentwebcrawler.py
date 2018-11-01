"""demo for the sync/ipc using queue"""
import requests
import multiprocessing
from requests.exceptions import ConnectionError
from json import load
from email.mime.text import MIMEText
from smtplib import SMTP

print(load((open('smtpps.json'))))


def send_alert_mail(**kwargs):
    """sending alert mail"""
    print(kwargs)
    smptp_server = kwargs.get('smtp')
    from_add = kwargs.get('from_address')
    to_addr = kwargs.get('to_address')
    subject = kwargs.get('subject')
    email_body = kwargs.get('body')

    msg = MIMEText(email_body)
    msg['from'] = from_add
    msg['To'] = to_addr
    msg['Subject'] = subject

    server = SMTP()
    server.connect(smptp_server)
    server.sendmail(from_add, to_addr, msg.as_string())
    server.close()


def web_crawler(q):
    """"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()
        payload = requests.get(url).content
        print("{}:{}:{}".format(p_name, url, payload[:128]))
    except ConnectionError as err:
        email_config = load(open('smtpps.json'))
        email_config['subject'] = "failed request by {}:{}".format(p_name, url)
        email_config['body'] = str(err)
        send_alert_mail(**email_config)


def main():
    """parent process"""
    queue_obj = multiprocessing.Queue()
    urls = ['http://python.org', 'http://linux.org', 'http://kernel.org/', 'http://goodfdfdfdfdfgle.com']

    for url in urls:
        child = multiprocessing.Process(target=web_crawler, args=(queue_obj,))
        child.start()

    for url in urls:
        queue_obj.put(url)  # add urls in to queue


if __name__ == '__main__':
    main()
