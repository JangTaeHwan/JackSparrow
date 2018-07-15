import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


TARGET_URL = 'https://torrent.mom/b/torrent_kortv_ent'

INPUT_FILE = open('the_latest_ents.txt', 'r')
OUTPUT_FILE = open('result.txt', 'w')

options = Options()
#options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--disable-gpu')

options.add_experimental_option("prefs", {
  "download.default_directory": "/home/tata8661/Work/JackSparrow",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

#driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=options)

def get_program_lists(url, output):
    driver.get(url)
    html = driver.execute_script("return document.documentElement.innerHTML;")

    soup = BeautifulSoup(html, "html.parser").find("tbody")
    rows = soup.find_all("td", {"class" : "td_subject"})

    for row in rows:
        link = row.find("a").get("href")
        subject = row.get_text()
        output.writelines(subject)
        output.writelines(link)

def download_torrent(url):
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "file/unknown");
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.download.dir", os.getcwd())
    profile.set_preference("pdfjs.disabled", True);

    driver2 = webdriver.Firefox(firefox_profile=profile)
    driver2.get(url)
#    driver2.find_element_by_xpath("(//a[@class='list-group-item break-word view_file_download at-tip'])[2]").click()
    driver2.find_element_by_xpath("//a[@class='view_file_download']").click()
#    driver2.quit()

def main():
    try:
#        get_program_lists(TARGET_URL, OUTPUT_FILE)
#        download_torrent("http://totoria.co/bbs/board.php?bo_table=torrent_kortv_ent&wr_id=31366")
        download_torrent("https://torrent.tax/b/torrent_kortv_ent-53019")
    except Exception as e:
        print("Exception: ", e)

#    driver.quit()
    OUTPUT_FILE.close()

if __name__ == '__main__':
    main()
