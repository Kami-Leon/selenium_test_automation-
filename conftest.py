import pytest
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options


url = 'https://demoqa.com/'

@pytest.fixture(scope="function", autouse=True)
def get_driver(request):
    # options = Options()
    # options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    # driver = webdriver.Firefox(options=options)

    # options.add_argument('--headless')
    driver = webdriver.Chrome()
    driver.get(url)
    request.cls.driver = driver
