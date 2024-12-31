import os
import requests
from bs4 import BeautifulSoup

# Base URL and sub-path
base_url = "https://eddirasa.com/ens-pri/first-primary/"
sub_path = "mathematics/"
url = base_url + sub_path

# Search criteria
criteria = "الأول"


# +++المواد+++
# mathematics/
# arabic/
# islamic/
# science-technologie/
# civic/
# music/
# art/
# french/
# english/
# tamazight/
# exercises/

# Function to fetch and save links
def fetch_and_save_links():
    print("Fetching links from main URL...")
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> tags containing the criteria in their text
            file_name = f"{sub_path.replace('/', '')}_{criteria}.txt"
            links = []

            for a_tag in soup.find_all('a'):
                text = a_tag.get_text()
                if criteria in text:
                    href = a_tag.get('href')
                    if href:
                        links.append(href)

            with open(file_name, 'w', encoding='utf-8') as file:
                file.write('\n'.join(links))

            print(f"Saved {len(links)} links to {file_name}")
            return file_name
        else:
            print(f"Failed to fetch the main URL. Status code: {response.status_code}")
            return None
    except Exception as error:
        print(f"Error fetching the main URL: {error}")
        return None

# Function to visit links and find specific files
def visit_links_and_save(file_name):
    print("Visiting links and searching for specific files...")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            links = file.read().splitlines()

        download_links = []

        for link in links:
            print(f"Visiting: {link}")
            try:
                response = requests.get(link)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')

                    for a_tag in soup.find_all('a'):
                        href = a_tag.get('href')
                        if href and href.startswith("https://eddirasa.com/wp-content/uploads") and (href.endswith(".pdf") or href.endswith(".docx")):
                            download_links.append(href)
                else:
                    print(f"Failed to fetch link: {link}. Status code: {response.status_code}")
            except Exception as error:
                print(f"Error visiting link {link}: {error}")

        download_file_name = f"downloads_from_{sub_path.replace('/', '')}.txt"
        with open(download_file_name, 'w', encoding='utf-8') as file:
            file.write('\n'.join(download_links))

        print(f"Saved {len(download_links)} download links to {download_file_name}")
    except Exception as error:
        print(f"Error reading the links file {file_name}: {error}")

# Main workflow
if __name__ == "__main__":
    file_name = fetch_and_save_links()
    if file_name:
        visit_links_and_save(file_name)
