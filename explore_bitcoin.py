import pandas
from datetime import date

bitcoin_data = pandas.read_csv('bitcoin_data.csv')
print(bitcoin_data)



test_date = date.fromtimestamp(1466953112)
print(test_date)


for row in bitcoin_data['date_unix']:
    #row['date'] = date.fromtimestamp(row['unix_date'])
    print(row)
    
print(bitcoin_data)