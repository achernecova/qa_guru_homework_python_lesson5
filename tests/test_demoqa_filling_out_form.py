import os
from time import sleep

from selene import be, browser, have, command
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_filling_out_form_selenium(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    sleep(5)
    driver.find_element(By.ID, "firstName").send_keys('Alexandra')
    driver.find_element(By.ID, "lastName").send_keys('Chernetsova')
    driver.find_element(By.ID, "userEmail").send_keys('achernecova@inbox.ru')
    driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
    driver.find_element(By.ID, "userNumber").send_keys('8123456789')
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']").click()
    driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']//*[@value='3']").click()

    driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']").click()
    driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']//*[@value='1991']").click()
    driver.find_element(By.XPATH, "//*[contains(@class, 'react-datepicker__day--019')]").click()

    driver.find_element(By.ID, "subjectsInput").click()
    driver.find_element(By.ID, "subjectsInput").send_keys("Biology")
    driver.find_element(By.ID, "subjectsInput").send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "//*[@for='hobbies-checkbox-2']").click()

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'les.jpg'
    )
    driver.find_element(By.ID, "uploadPicture").send_keys(file_path)
    driver.find_element(By.ID, "currentAddress").send_keys('Москва')

    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.ID, "state"))
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.ID, "react-select-3-input").send_keys("Haryana", Keys.ENTER)

    driver.find_element(By.ID, "city").click()
    driver.find_element(By.ID, "react-select-4-input").send_keys("Karnal", Keys.ENTER)

    driver.find_element(By.ID, "submit").click()

    expected_texts = [
        'Alexandra Chernetsova',
        'achernecova@inbox.ru',
        'Female',
        '8123456789',
        '19 April,1991',
        'Biology',
        'Reading',
        'les.jpg',
        'Москва',
        'Haryana Karnal'
    ]
    elements = driver.find_elements(By.CSS_SELECTOR, '.modal-content table tbody tr td:nth-child(2)')
    actual_texts = [elem.text for elem in elements]

    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class='modal-title h4']"))
    )
    assert driver.find_element(By.XPATH, "//*[@class='modal-title h4']").text == "Thanks for submitting the form"
    assert actual_texts == expected_texts, f"Ожидалось: {expected_texts}, но получено: {actual_texts}"


def test_filling_out_form_selene():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element("#firstName").type('Alexandra')
    browser.element("#lastName").type('Chernetsova')
    browser.element("#userEmail").type('achernecova@inbox.ru')
    browser.element('[for="gender-radio-2"]').should(be.clickable).click()
    browser.element("#userNumber").type('8123456789')
    browser.element("#dateOfBirthInput").click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="3"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1991"]').click()
    browser.element((By.XPATH, "//*[contains(@class, 'react-datepicker__day--019')]")).click()

    browser.element("#subjectsInput").type("Biology").press_enter()
    browser.element((By.XPATH, "//*[@for='hobbies-checkbox-2']")).click()

    file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'les.jpg'
    )
    browser.element("#uploadPicture").type(file_path)
    browser.element("#currentAddress").type('Москва')

    browser.element("#state").perform(command.js.scroll_into_view).click()
    browser.element("#react-select-3-input").type("Haryana").press_enter()

    browser.element("#city").click()
    browser.element("#react-select-4-input").send_keys("Karnal").press_enter()

    browser.element("#submit").click()
    browser.element(".modal-title.h4").should(have.text("Thanks for submitting the form"))

    browser.all('.modal-content table tbody tr td:nth-child(2)').should(have.exact_texts(
        'Alexandra Chernetsova',
        'achernecova@inbox.ru',
        'Female',
        '8123456789',
        '19 April,1991',
        'Biology',
        'Reading',
        'les.jpg',
        'Москва',
        'Haryana Karnal'
    ))