from selenium import webdriver
from selenium.webdriver.common.by import By
import time

input_email = "qa.rakamin.jubelio@gmail.com"
input_password = "Jubelio123!"

driver = webdriver.Chrome()
url = "https://app.jubelio.com/login"
driver.get(url)

email = driver.find_element(By.NAME, 'email')
email.send_keys(input_email)
time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.send_keys(input_password)
time.sleep(2)

login = driver.find_element(By.XPATH, "//button[@class='ladda-button btn btn-primary block full-width mb-4']")
login.click()

while True:
    pass