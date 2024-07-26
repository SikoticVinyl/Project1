import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Steam Charts page for Ark now since we have the Isle
url = "https://steamcharts.com/app/275850" 

# Fetch the page content
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

# Parse the page content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the player data
table = soup.find('table', class_='common-table')

# Extract the headers
headers = [header.text.strip() for header in table.thead.find_all('th')]

# Extract the data rows
data = []
for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    month = columns[0].text.strip()
    avg_players = columns[1].text.strip()
    peak_players = columns[4].text.strip()
    data.append([month, avg_players, peak_players])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Month', 'Avg Players', 'Peak Players'])

# Save the DataFrame to a CSV file
df.to_csv('nomansky_player_data.csv', index=False)

print("Data has been successfully scraped and saved to 'nomansky_player_data.csv'")
