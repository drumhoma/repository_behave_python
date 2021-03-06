from behave import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Откроем главную страницу. Передадим в качестве аргумента адрес страницы.
@given("website '{url}'")
def step(context, url):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get(url)


# Введем поисковый запрос "Тест"
@when("search text '{text}'")
def step(context, text):
    context.browser.find_element(By.XPATH, "//input[@name='text']").send_keys(f"{text}")


# Теперь нажмем на кнопку "Найти"
@when("push button with text '{text}'")
def step(context, text):
    button = WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.XPATH, "//button")))
    button_text = button.text
    button.click()
    assert button_text == f'{text}', f"Кнопка '{text}' не найдена"


# Проверим, что на странице с результатами поиска есть искомый текст
@then("page include text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 3).until(
        EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
    context.browser.quit()

    # try:
    #     text = WebDriverWait(context.browser, 3).until(
    #         EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text}')]")))
    # except TimeoutException:
    #     return False
    # return True
    # assert text != '{text}', f"В тексте нет слова'{text}'"
