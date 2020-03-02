from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from pathlib import Path

def BNHAGGA():
    #mailing list for this specific anime
    mailing_list = ['noor_yadallee@hotmail.com']

    #link to website that will be scraped
    BNHA = 'https://www12.gogoanime.io/category/boku-no-hero-academia-4th-season'

    #scraping to retrieve latest episode
    heroClient = uReq(BNHA)
    BNHAGGA_html = heroClient.read()
    heroClient.close()

    hero_soup = soup(BNHAGGA_html, 'html.parser')
    containers = hero_soup.findAll('a', {'class' : 'active'})
    current = containers[0].text[2:]

    #storing info in a file on server computer
    data = Path('C:\\Users\\User\\Desktop\\Coding\\Python\\WebScraping\\Animes')
    filename = data/'BNHA.txt'

    #write recently fetched episode into file
    with  open(filename, 'a') as f:
        f.write('\n' + current)

    with  open(filename, 'r') as f:
        lines = f.readlines()
        prev_last = lines[len(lines) - 2].strip()
        last = lines[len(lines) - 1]

        #display previously checked and most recent episode in console
        print('My Hero Academia Season 4:')
        print('Previous check:' + prev_last)
        print('Most recent check:' + last)
        print()

    #check whether a new episode has been released
    if int(last) > int(prev_last):
        mail('My Hero Academia', BNHA, mailing_list)
        return True

def haikyuuGGA():
    #mailing list for this specific anime
    mailing_list = ['noor_yadallee@hotmail.com']

    #link to website that will be scraped
    haikyuu = 'https://www15.gogoanime.io/category/haikyuu-to-the-top'

    #scraping to retrieve latest episode
    volleyClient = uReq(haikyuu)
    haikyuu_html = volleyClient.read()
    volleyClient.close()

    volley_soup = soup(haikyuu_html, 'html.parser')
    containers = volley_soup.findAll('a', {'class' : 'active'})
    current = containers[0].text[2:]

    #storing info in a file on server computer
    data = Path('C:\\Users\\User\\Desktop\\Coding\\Python\\WebScraping\\Animes')
    filename = data/'volleyball.txt'

    #write recently fetched episode into file
    with  open(filename, 'a') as f:
        f.write('\n' + current)

    with  open(filename, 'r') as f:
        lines = f.readlines()
        prev_last = lines[len(lines) - 2].strip()
        last = lines[len(lines) - 1]

        #display previously checked and most recent episode in console
        print('Haikyuu to the top:')
        print('Previous check:' + prev_last)
        print('Most recent check:' + last)
        print()

    #check whether a new episode has been released
    if int(last) > int(prev_last):
        mail('haikyuu', haikyuu, mailing_list)
        return True

def dorohedoroGGA():
    #mailing list for this specific anime
    mailing_list = ['noor_yadallee@hotmail.com']

    #link to website that will be scraped
    dorohedoro = 'https://www15.gogoanime.io/category/dorohedoro'

    #scraping to retrieve latest episode
    dorohedoroClient = uReq(dorohedoro)
    dorohedoro_html = dorohedoroClient.read()
    dorohedoroClient.close()

    dorohedoro_soup = soup(dorohedoro_html, 'html.parser')
    containers = dorohedoro_soup.findAll('a', {'class' : 'active'})
    current = containers[0].text[2:]

    #storing info in a file on server computer
    data = Path('C:\\Users\\User\\Desktop\\Coding\\Python\\WebScraping\\Animes')
    filename = data/'dorohedoro.txt'

    #write recently fetched episode into file
    with  open(filename, 'a') as f:
        f.write('\n' + current)

    with  open(filename, 'r') as f:
        lines = f.readlines()
        prev_last = lines[len(lines) - 2].strip()
        last = lines[len(lines) - 1]

        #display previously checked and most recent episode in console
        print('Dorohedoro:')
        print('Previous check:' + prev_last)
        print('Most recent check:' + last)
        print()
    if int(last) > int(prev_last):
        print('New episode is out, sending mail to recipients')
        mail('dorohedoro', dorohedoro, mailing_list)
        return True

def mail(name, link, mailing_list):
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
        body = 'You can now watch {} at {}'.format(name, link)

        msg = f'Subject: {subject}\n\n{body}'

        #send to mailing list
        for recipient in mailing_list:
            smtp.sendmail('anime.manga.notifs@gmail.com', recipient, msg)


while True:
    #run script every 12 hours
    import time
    time.sleep(43200)

    print('Checking for new episodes')
    print()

    PlusUltra = False
    PlusUltra = BNHAGGA()

    karasuno = False
    karasuno = haikyuuGGA()

    dorohedoro = False
    dorohedoro = dorohedoroGGA()

    print()
    print()
