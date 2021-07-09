from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://runescape.wiki/w/Travelling_Merchant%27s_Shop")

test = driver.find_elements_by_class_name("inventory_image a")

print(test)
driver.quit()
