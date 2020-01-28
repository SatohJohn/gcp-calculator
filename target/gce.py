import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        num = str(row[0].value)
        machineType = str(row[1].value)
        location = str(row[2].value)
        timeCount = str(row[3].value)
        timeType = str(row[4].value)

        function_root_selector = 'form[name="ComputeEngineForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[name="quantity"]').send_keys(num)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.computeServer.instance"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'md-select-menu md-option[value="{}"]'.format(machineType)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.computeServer.location"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(location)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.computeServer.timeType"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(timeType)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[name="{}"]'.format(timeType)).clear()
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[name="{}"]'.format(timeType)).send_keys(timeCount)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
