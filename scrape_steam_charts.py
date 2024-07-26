import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import time

async def fetch_html(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_monthly_player_counts(appid):
    url = f'https://steamcharts.com/app/{appid}'
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract data table containing historical player counts
    table = soup.find('table', class_='common-table')
    dates = []
    avg_players = []
    gain = []
    peak_players = []
    
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            cols = row.find_all('td')
            if len(cols) >= 5:
                dates.append(cols[0].text.strip())
                avg_players.append(cols[1].text.strip().replace(',', ''))
                gain.append(cols[2].text.strip().replace(',', ''))
                peak_players.append(cols[4].text.strip().replace(',', ''))
    
    # Respectful rate limiting
    time.sleep(2)  # Delay between requests
    
    return pd.DataFrame({
        'Date': pd.to_datetime(dates, format='%b %Y'),
        'Avg Players': pd.to_numeric(avg_players, errors='coerce'),
        'Gain': pd.to_numeric(gain, errors='coerce'),
        'Peak Players': pd.to_numeric(peak_players, errors='coerce')
    })

async def main():
    # Define the app ID for The Isle
    appid = 376210
    
    # Fetch monthly player counts for The Isle
    df = await fetch_monthly_player_counts(appid)
    
    # Save data to a CSV file
    df.to_csv('The_Isle_monthly_player_counts.csv', index=False)
    print("Saved The Isle monthly player counts to CSV.")

# Run the script
asyncio.run(main())
