"""Scrape stack overflows first ten pages for jobs."""
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


base_url = 'https://stackoverflow.com/jobs?med=site-ui&ref=jobs-tab'

def job_scraper(base_url):
    url_list = []
    for x in range(10):
        x += 1
        url_list.append(base_url + '&pg={}'.format(x))
    for url in url_list:
        # page = requests.get(url, verify=False)
        page = urlopen(url)
        soup = bs(page)
        tags = soup.find_all('a', class_='post-tag job-link no-tag-menu')
        import pdb; pdb.set_trace()
        # for tag in tags:


job_scraper(base_url)



# - The job title
# - The company name 
# - The location
# - The date posted (in whatever date format makes the most sense to you)
# - The link to the actual job posting