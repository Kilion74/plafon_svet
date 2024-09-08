import bs4
import time
import csv
from selenium import webdriver  # pip install selenium
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # pip install webdriver-manager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36')
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                      options=chrome_options) as driver:  # Открываем хром
    driver.get("https://donplafon.ru/catalog/lyustry/podvesnye/")  # Открываем страницу
    time.sleep(3)  # Время на прогрузку страницы
    soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')

    heads = soup.find_all('div', {'class': 'productItem__container'})
    print(len(heads))
    for i in heads:
        link = i.find_next('div', {'class': 'madSlider__list grab'}).find('a', href=True)
        print('https://donplafon.ru'+link['href'])
        # with webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        #                       options=chrome_options) as driver:  # Открываем хром
        #     driver.get(url)  # Открываем страницу
        #     time.sleep(2)  # Время на прогрузку страницы
        #     block = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        #     name = block.find('h1', {'productInfo__title fn'}).text.strip()
        #     print(name)
        #     price = block.find('div', {'class': 'buy-info__p-new'}).text.strip()
        #     print(price)
        #     nalichiye = block.find('div', {'class': 'buy-info__avail'}).text.strip()
        #     print(nalichiye)
        #     params = block.find_all('div', {'class': 'pr-page__span'})
        #     print(params[0].text.strip())
        #     brand = (params[0].text.strip())
        #     print(params[1].text.strip())
        #     articul = (params[1].text.strip())
        #     print('\n')
        #
        #     storage = {'name': name, 'price': price, 'nalichiye': nalichiye, 'brand': brand, 'articul': articul}
        #
        #     fields = ['Name', 'Price', 'Nalichiye', 'Brand', 'Articul']
        #     with open('lustry.csv', 'a+', encoding='utf-16') as f:
        #         pisar = csv.writer(f, delimiter=';', lineterminator='\r')
        #         # Проверяем, находится ли файл в начале и пуст ли
        #         f.seek(0)
        #         if len(f.read()) == 0:
        #             pisar.writerow(fields)  # Записываем заголовки, только если файл пуст
        #         pisar.writerow(
        #             [storage['name'], storage['price'], storage['nalichiye'], storage['brand'], storage['articul']])
