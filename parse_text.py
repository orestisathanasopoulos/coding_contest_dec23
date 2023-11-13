from bs4 import BeautifulSoup
import requests



r = requests.get('https://fr.wikipedia.org/wiki/Ginkgo')


soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

for link in soup.find_all('a', string='Ginkgo', limit=3):
    link = requests.get(link.get('href'))
    print(BeautifulSoup(link.text,'html.parser'))


