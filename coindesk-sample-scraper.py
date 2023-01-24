import requests
from bs4 import BeautifulSoup
import mysql.connector

# Connect to MySQL database
cnx = mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_db')
cursor = cnx.cursor()

# Create table to store news data
cursor.execute('''CREATE TABLE IF NOT EXISTS news
                 (title TEXT, article TEXT, date DATE)''')

# Scrape news articles from website
url = 'https://www.coindesk.com/category/technology-news'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# Extract title, article, and date from each article
for article in soup.find_all('article'):
    title = article.find('h2').text
    text = article.find('p').text
    date = article.find('time')['datetime']
    # Store data in MySQL database
    cursor.execute("INSERT INTO news (title, article, date) VALUES (%s, %s, %s)", (title, text, date))
    cnx.commit()

# Close connection to database
cnx.close()
