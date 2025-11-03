import pytest
from selene import browser


@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.page_load_strategy = 'none'
    chrome_options.add_argument("--window-size=1280,900")

    # Todo - для firefox другие переменные передаются в расширение:
    # chrome_options.add_argument("--width=1920")
    # chrome_options.add_argument("--height=1080")
    driver = webdriver.Chrome(options=chrome_options)

    # Передаем драйвер в Selene
    browser.config.driver = driver

    yield driver

    driver.quit()
