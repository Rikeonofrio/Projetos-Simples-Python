import imp
import profile
import requests
from bs4 import BeautifulSoup as bs

githubUser = input('Coloque seu github: ')
url = 'https://github.com/'+githubUser
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profileIamge = soup.find('img',{'alt': 'Avatar'})['src']
print(profileIamge)