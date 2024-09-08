import requests # pip install requests
from bs4 import BeautifulSoup # pip install bs4
# pip install lxml


url = 'https://www.vamsvet.ru/catalog/section/svetilniki_nastennye/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Connactoin': 'keep-alive'}
data = requests.get(url, headers=headers).text
block = BeautifulSoup(data, 'lxml')
heads = block.find_all('div', {'class': 'prod__el'})
print(len(heads))
