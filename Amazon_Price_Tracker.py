# Step 1: Import the necessary ibrary
import requests
from bs4 import BeautifulSoup as bs
import smtplib
import ssl
from email.message import EmailMessage

# Step 2: Define the URL and Create the User Agent Info:
URL = 'https://www.amazon.in/Apple-iPhone-13-128GB-Green/dp/B09V4B6K53/ref=sr_1_2_sspa?crid=2W9R625KR5YQN&keywords=iphone&qid=1687616393&sprefix=iphone%2Caps%2C421&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
header = {'User-Agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254'}

# Step 3: Create the Price Extractor Fuction
def extract_price():
    page = requests.get(URL, headers = header)
    soup = bs(page.content, 'html.parser')
    price = float(soup.find('span', class_ = 'a-price-whole').text.split()[0].replace(",",""))
    return price

# Step 4: Create the Email Notifier Function
def notify():
    port = 465    # for SSL
    smtp_server = "smtp.gmail.com"
    sender_mail = "lokhandedhananjay97@gmail.com"
    receiver_mail = "lokhandedhananjay97@gmail.com"
    password = 'aoxornxmiyewpgvg'
    subject = 'BUY NOW!'
    message = f"""
    Price has Dropped! Buy your product now!
    Link: {URL}
    """
    em = EmailMessage()
    em['From'] = sender_mail
    em['To'] = receiver_mail
    em['subject'] = subject
    em.set_content(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_mail, password)
        server.sendmail(sender_mail, receiver_mail, em.as_string())
        print('Message Sent')

# Step 5: Create the Driver Code
my_price = 70000
if extract_price() <= my_price:
    notify()
