import requests
import time

def get_messages_by_site():
    
    
    url = 'https://www.thiswebsitewillselfdestruct.com/api/get_letter'
    page = requests.get(url)
    message = page.json()
    
    for symbol in message['body']:
        if symbol in alphabet:
            return message['body']


alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    
while True:
    result = get_messages_by_site()
    
    if result == str(result):
        print(result)
        
    time.sleep(1)