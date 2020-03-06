from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pathlib import Path

def scrape(name, link, prev, mailing_list):
    #scraping to retrieve latest episode
    Client = uReq(link)
    site_html = Client.read()
    Client.close()

    _soup = soup(site_html, 'html.parser')
    containers = _soup.findAll('a', {'class' : 'active'})

    current = int(containers[0].text[2:])

    if current > prev:
        print('sending mail')
        current = mail(name, link, current, mailing_list)

    else :
        print('NOT sending mail')
    return current

def mail(name, link, current, mailing_list):
    import smtplib

    #context manager to automatically close the connection
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        #identify ourselves to the mail server with ehlo
        smtp.ehlo()
        #encrytp connection
        smtp.starttls()
        #re-identify ourselves to the mail server with ehlo
        smtp.ehlo()

        #login into mail server
        smtp.login('anime.manga.notifs@gmail.com', 'qwErty123!')

        #email
        subject = 'New episode of {} is out'.format(name)
        body = 'You can now watch {} episode {} at {}'.format(name, current, link)

        msg = f'Subject: {subject}\n\n{body}'

        #send to mailing list
        for recipient in mailing_list:
            smtp.sendmail('anime.manga.notifs@gmail.com', recipient, msg)
        return current

animes = [['Boku No Hero Academia', 0], ['Haikyuu', 0]]
mailings = {
'Boku No Hero Academia' : ['https://www12.gogoanime.io/category/boku-no-hero-academia-4th-season','noor_yadallee@hotmail.com'],

'Haikyuu' : ['https://www15.gogoanime.io/category/haikyuu-to-the-top','noor_yadallee@hotmail.com'],

'dorohedoro' : ['https://www15.gogoanime.io/category/dorohedoro','noor_yadallee@hotmail.com']
}

while True:
    import time
    time.sleep(43200)
    for i in range(0, len(animes)):
        name = animes[i][0]
        link, mailing_list = mailings[name][0], mailings[name][1:]
        prev = animes[i][1]

        print(animes[i][0],animes[i][1])
        animes[i][1] = scrape(name, link, prev, mailing_list)
        print(animes[i][1])
