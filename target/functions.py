import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        name = row[0].value
        executionTime = str(row[1].value)
        preRequest = str(row[2].value)
        requestNum = str(row[3].value)

        function_root_selector = 'form[name="FunctionsForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.functions.name"][name="name"]').send_keys(name)

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + 'md-select[ng-model="listingCtrl.functions.type"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'md-option[value="256-400"]').click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.functions.executionTime"][name="executionTime"]').send_keys(executionTime)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.functions.bandwidth.value"][name="bandwidth"]').send_keys(preRequest)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.functions.invocationsCount"][name="invocationsCount"]').send_keys(requestNum)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
