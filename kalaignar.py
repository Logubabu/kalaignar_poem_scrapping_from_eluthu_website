from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re

chrome_options = Options()
chrome_options.add_argument("log-level=3")  # disable logging
# chrome_options.add_argument("--headless")  # run in headless mode
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--ignore-ssl-errors")

PATH = r"D:/chromedriver.exe"
browser = webdriver.Chrome(PATH, chrome_options=chrome_options)
browser.get('https://eluthu.com/kavignar/Karunanidhi.php')
browser.maximize_window()
soup = BeautifulSoup(browser.page_source, "html.parser")
lists = soup.find("div", attrs={"id": "tholar_list"})
browser.find_element(
    By.XPATH, '//*[@id="tholar_list"]/table/tbody/tr[2]/td[1]/a').click()

sleep(5)
for x in range(39):
    res = BeautifulSoup(browser.page_source, "html.parser")
    h1 = res.find("h1", attrs={"class": "post_title"})
    p1 = res.find("p", attrs={"class": "post_desc"})

    title = re.sub(r'[?|$|.|!]', r'', h1.text)

    content = re.sub(r'[|$||*]', r' ', p1.text)
    try:
        with open(f'{title}.txt', 'w', encoding='utf-8') as f:
            f.write(f'{content}')
            sleep(2)
    except Exception as e:
        print(e)

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)
    try:
        browser.find_element(
            By.XPATH,
            '/html/body/div[6]/div[1]/div[10]/div[2]/span/a').click()
    except Exception as e:
        break
print("Finish")

browser.quit()  #to close window
