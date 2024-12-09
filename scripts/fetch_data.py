import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_webpage(url):
    """
    Fetch the content of the webpage.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to fetch webpage: {response.status_code}")
        return None

def parse_data(content):
    """
    Parse the HTML content and extract the relevant data.
    """
    soup = BeautifulSoup(content, 'html.parser')
    data = []

    # Example: Adjust this part to match the actual structure
    history_section = soup.find('div', {'id': 'history-rounds'})
    if history_section:
        for div in history_section.find_all('div', class_='round'):
            round_data = [span.text for span in div.find_all('span', class_='spin-result')]
            if round_data:
                data.append(round_data)

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['Spin Result'])
    return df

def save_data(data, file_path):
    """
    Save the data to a CSV file.
    """
    data.to_csv(file_path, index=False)
    print(f"Data saved to: {file_path}")

if __name__ == "__main__":
    # URL of the webpage to scrape
    url = 'https://gamblingcounting.com/evolution-roulette'
    
    # Fetch the webpage content
    content = fetch_webpage(url)
    
    if content:
        # Parse the data
        data = parse_data(content)
        
        if data is not None:
            # Save the data
            save_path = '../data/roulette_history.csv'
            save_data(data, save_path)
