from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# Път към ChromeDriver (съвместим с Brave)
driver_path = "C:\\Drivers\\chromedriver.exe"  # Замени с твоя път

# chrome driver trqbva da e 131
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  # Замени с твоя път

# change browser to brave
options = Options()
options.binary_location = brave_path  # Уusing brave browser

# session start
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

phone_numbers = [
    "0887123456", "0885123487", "0879623457", "0883456789", "0894567123",
    "0897654321", "0878123456", "0889432765", "0891234567", "0876543298",
    "0881765432", "0894321567", "0879234516", "0886534219", "0893456721",
    "0878423156", "0883245679", "0895627348", "0879431256", "0887523649",
    "0896342571", "0872156349", "0889432761", "0891276534", "0876342591",
    "0884231756", "0893527614", "0876534912", "0881342765", "0897215346",
    "0874569231", "0887523694", "0892431756", "0879645321", "0882156437",
    "0891342765", "0873456912", "0889432516", "0895643271", "0874231596",
    "0882345671", "0897432156", "0879624351", "0886523417", "0895236714",
    "0879432516", "0887342159", "0891634527", "0875346921", "0889264357"
]

try:
    # PAge loads
    url = "https://byivan.bg/wonder.html"  # site url
    driver.get(url)
    time.sleep(3)  # wait for the page to load

    #  fill and click
    for i in range(2):  # 50 orders

        phone_number = phone_numbers[i % len(phone_numbers)]

        # Pick a color
        color_dropdown = driver.find_element(By.XPATH, "//*[@id='params[412]']")  # Замени с точния XPATH или ID
        color_dropdown.click()
        time.sleep(1)

        # first element drop down click
        color_option = driver.find_element(By.XPATH, "//*[@id='params[412]'']/option[2]")  # Замени с реалния селектор
        color_option.click()

        # tel number - waiting for TEDO
        phone_field = driver.find_element(By.XPATH, "//*[@id='fast-order-phone']")  # Замени с точния селектор
        phone_field.send_keys(phone_number)

        # agree with the checkbox
        agreement_checkbox = driver.find_element(By.XPATH, "//*[@id='quickOrderTermsConsent']")  # Замени с реалния селектор
        agreement_checkbox.click()

        # click Order button
        order_button = driver.find_element(By.XPATH, "//*[@id='fast-order-send']")  # Замени със селектора на бутона
        order_button.click()

        print(f"Поръчка {i + 1} направена.")
        time.sleep(2)  # Изчаква страницата да се обнови след поръчката

        # back to the loop
        driver.refresh()
        time.sleep(3)

finally:
    # closing session of the browser
    time.sleep(5)
    driver.quit()