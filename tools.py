import requests
from bs4 import BeautifulSoup

def fetch_company_details(url):
    """
    Scrape the company name and body text from the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title')
        company_name = title.get_text().strip() if title else "Company name not found"
        body_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return company_name, body_text
    except Exception as e:
        return None, f"An error occurred during scraping: {str(e)}"
