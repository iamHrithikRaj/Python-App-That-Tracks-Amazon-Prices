import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JXDZFM/ref=sr_1_1_sspa?dchild=1&keywords=macbook&qid=1592241660&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUE3OE9EVDNFUzlMTDImZW5jcnlwdGVkSWQ9QTAyMDEzNTkxSkhVVUdSQ0xFSTJPJmVuY3J5cHRlZEFkSWQ9QTA0ODM5NTQyM0xFRFlBTlM1V09GJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0"}


def check_price():
  page = requests.get(URL, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')
  # print(soup.prettify())

  productTitle = soup.find(id='productTitle').get_text()
  price = soup.find(id='priceblock_ourprice').get_text()
  temp = ''
  for n in price[2:-3]:
      if n != ',':
          temp += n
  productPrice = int(temp)

  if productPrice > 185000:
      send_email()

  print(productPrice)
  print(productTitle.strip())


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hraj2661999@gmail.com', 'qyzeetztyetwsqqi')

    subject = "Price just fell down!"
    body ="Price just fell down!\nCheck the link"+URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'hraj2661999@gmail.com',
        'hraj2661999@gmail.com',
        msg
    )
    print('HEY! MAIL HAS BEEN SENT')

    server.quit()


check_price()