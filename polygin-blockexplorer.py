import json
import requests
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to MySQL database
cnx = mysql.connector.connect(user='your_username', password='your_password', host='your_host', database='your_db')
cursor = cnx.cursor()

# Create table to store blockchain data
cursor.execute('''CREATE TABLE IF NOT EXISTS blockchain_data
                 (block_number INTEGER, timestamp INTEGER, transactions INTEGER)''')

# Get blockchain data from Polygon API
url = 'https://api.thepolygon.network/v1/eth/blocks?limit=100'
response = requests.get(url)
data = json.loads(response.text)

# Extract relevant data and store in MySQL database
for block in data:
    block_number = block['number']
    timestamp = block['timestamp']
    transactions = block['transactions']
    cursor.execute("INSERT INTO blockchain_data (block_number, timestamp, transactions) VALUES (%s, %s, %s)", (block_number, timestamp, transactions))
    cnx.commit()

# Close connection to database
cnx.close()

# Load data into pandas dataframe
df = pd.read_sql("SELECT * from blockchain_data", cnx)

# Create line chart of transactions per block
plt.plot(df['block_number'], df['transactions'])
plt.xlabel('Block Number')
plt.ylabel('Transactions')
plt.title('Transactions per Block')
plt.show()
