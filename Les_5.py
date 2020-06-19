from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pprint import pprint
from pymongo import MongoClient
import time

driver = webdriver.Chrome(r"C:\Users\Wankin\PycharmProjects\OOP\chromedriver.exe")
driver.get("https://mail.ru")
list_of_letters_data = []


def login_in():
    elem = driver.find_element_by_id("mailbox:login")
    elem.send_keys("study.ai_172@mail.ru")
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, 'mailbox:submit')))
    button.click()
    elem = driver.find_element_by_id("mailbox:password")
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "mailbox:password")))
    elem.send_keys("NextPassword172")
    elem = driver.find_element_by_id("mailbox:submit")
    return elem.submit()


def find_add_letters(q_letters):
    links_without = driver.find_elements_by_class_name("js-letter-list-item")
    list_l = []
    for i in links_without:
        a = i.get_attribute("href")
        list_l.append(a)
    index = q_letters - 1
    for l in list_l:
        item = {}
        driver.get(l)
        time.sleep(3)
        author = driver.find_element_by_class_name("letter-contact")
        author_of_letter = author.get_attribute("title")
        date = driver.find_element_by_class_name("letter__date")
        date_of_letter = date.text
        theme = driver.find_element_by_class_name("thread__subject")
        theme_of_letter = theme.text
        text = driver.find_element_by_class_name("js-readmsg-msg")
        text_of_letter = text.text
        item["author"] = author_of_letter
        item["date"] = date_of_letter
        item["theme"] = theme_of_letter
        item["text"] = text_of_letter
        list_of_letters_data.append(item)
        if l == list_l[index]:
            break
    return pprint(list_of_letters_data)


login_in()
time.sleep(5)


q_letters = 4
find_add_letters(q_letters)


# client = MongoClient("192.168.0.107", 27017)
# db = client["mail_letters"]
# letters_mail = db.letters_mail
# letters_mail.insert_many(list_of_letters_data)
