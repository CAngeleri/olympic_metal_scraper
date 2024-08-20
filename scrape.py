import requests
from bs4 import BeautifulSoup
import json

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table'

# Send a GET request to fetch the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the medal counts
table = soup.find('table', {'class': 'wikitable'})

# Extract the rows from the table
rows = table.find_all('tr')

# Initialize an empty list to store the data
medal_data = []

# Iterate over the rows and extract the data
for i, row in enumerate(rows):
    # Skip the header row
    if i == 0:
        continue

    # Extract columns
    cols = row.find_all('td')
    if len(cols) < 4:
        continue

    # Extract data from table - country and medal counts
    country = cols[0].a.text.strip()
    gold = cols[11].text.strip()
    silver = cols[12].text.strip()
    bronze = cols[13].text.strip()
    total_medals = cols[15].text.strip()

    # Append data to the list
    medal_data.append({
        'Country': country,
        'Total Medals': total_medals,
        'Gold Medals' : gold,
        'Silver Medals' : silver,
        'Bronze Medals' : bronze,
    })

# Keep only the first 10 countries - for officiant/faster testing
medal_data = medal_data[:10]

# Save the data to a JSON file - Parameters - 'file name','action type' w for write
with open('medal_counts.json', 'w') as f:
    json.dump(medal_data, f, indent=2)

print("Data saved to medal_counts.json")
