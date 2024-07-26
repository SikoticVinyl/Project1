import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import time

async def fetch_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            return await response.text()

async def fetch_monthly_player_counts(appid):
    url = f'https://steamcharts.com/app/{appid}'
    html = await fetch_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find('table', class_='common-table')
    dates = []
    avg_players = []
    gain = []
    percent_gain = []
    peak_players = []
    
    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                date_text = cols[0].text.strip()
                if "Last 30 Days" in date_text or "Month Avg." in date_text:
                    continue
                dates.append(date_text)
                avg_players.append(cols[1].text.strip().replace(',', ''))
                gain.append(cols[2].text.strip().replace(',', ''))
                percent_gain.append(cols[3].text.strip().replace('%', '').replace('+', ''))
                peak_players.append(cols[4].text.strip().replace(',', ''))
    
    time.sleep(2)  # Respectful rate limiting
    
    return pd.DataFrame({
        'Date': pd.to_datetime(dates, format='%b %Y', errors='coerce'),
        'Avg Players': pd.to_numeric(avg_players, errors='coerce'),
        'Gain': pd.to_numeric(gain, errors='coerce'),
        'Percent Gain': pd.to_numeric(percent_gain, errors='coerce'),
        'Peak Players': pd.to_numeric(peak_players, errors='coerce')
    })

async def main():
    appid = 376210  # App ID for The Isle
    
    df = await fetch_monthly_player_counts(appid)
    
    df.dropna(subset=['Date'], inplace=True)  # Remove rows with invalid dates
    
    df.to_csv('The_Isle_monthly_player_counts.csv', index=False)
    print("Saved The Isle monthly player counts to CSV.")

# Run the script
asyncio.run(main())

