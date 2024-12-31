import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://eddirasa.com/ens-pri/first-primary/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all divs with the class 'one_half last'
    divs = soup.find_all('div', class_='one_half')
    
    # Extract and print the href values of child <a> tags
    for div in divs:
        a_tag = div.find('a')
        if a_tag and 'href' in a_tag.attrs:
            print(a_tag['href'])
else:
    print(f"Failed to retrieve the page: {response.status_code}")