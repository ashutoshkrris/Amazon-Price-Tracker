from selenium import webdriver

DIRECTORY = 'reports'
NAME = str(input('Which product do you wish to look for ? \n'))
CURRENCY = '₹'
MIN_PRICE = str(input('What should be the minimum price in ₹ ? \n'))
MAX_PRICE = str(input('What should be the maximum price in ₹ ? \n'))
FILTERS = {
    'min' : MIN_PRICE,
    'max' : MAX_PRICE
}
BASE_URL = 'https://www.amazon.in/'


def get_chrome_driver(options):
    return webdriver.Chrome('./chromedriver.exe', chrome_options=options)

def get_chrome_options():
    return webdriver.ChromeOptions()

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')

def set_browser_as_incognito(options):
    options.add_argument('--incognito')