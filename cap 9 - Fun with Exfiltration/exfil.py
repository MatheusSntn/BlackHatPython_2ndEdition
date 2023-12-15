from win32com import client
import os
import random
import requests
import time
from private_credentials import username_site, password_site, api_key

username = str(username_site)
password = str(password_site)
api_dev_key = str(api_key)

def plain_paste(title, contents):
    login_url = 'https://pastebin.com/api/api_login.php'
    login_data = {
        'api_dev_key': api_dev_key,
        'api_user_name': username,
        'api_user_password': password,
    }
    r = requests.post(login_url, data=login_data)
    api_user_key = r.text

    paste_url = 'https://pastebin.com/api/api_post.php'
    paste_data = {
        'api_paste_name': title,
        'api_paste_code': contents.decode(),
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_option': 'paste',
        'api_paste_private': 0,
    }

    r = requests.post(paste_url,  data=paste_data)
    print(r.status_code)
    print(r.text)

def wait_for_browser(browser):
    while browser.ReadyState != 4 and browser.ReadyState != 'complete':
        time.sleep(0.1)
    
    def random_sleep():
        time.sleep(random.randint(5, 10))
        