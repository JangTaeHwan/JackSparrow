from bs4 import BeautifulSoup
from selenium import webdriver


TARGET_URL = 'https://torrent.mom/b/torrent_kortv_ent'

INPUT_FILE = open('the_latest_ents.txt', 'r')
OUTPUT_FILE = open('result.txt', 'w')

def crawl(url, output):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.execute_script("return document.documentElement.innerHTML;")

    soup = BeautifulSoup(html, "lxml").find("table", {"id" : "resultsTable"}).find("tbody")
    soup = BeautifulSoup(INPUT_FILE.read(), "html.parser").find("tbody")
    rows = soup.find_all("td", {"class" : "td_subject"})

    for row in rows:
        link = row.find("a").get("href")
        subject = row.get_text()
        output.writelines(subject)
        output.writelines(link)

def main():
    crawl(TARGET_URL, OUTPUT_FILE)
    OUTPUT_FILE.close()

if __name__ == '__main__':
    main()
