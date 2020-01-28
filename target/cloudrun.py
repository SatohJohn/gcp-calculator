import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        name = str(row[0].value)
        executionTime = str(row[1].value)
        dataRequest = str(row[2].value)
        requestNum = str(row[3].value)
        location = 'asia-northeast1'

        function_root_selector = 'form[name="RunForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.run.name"][name="name"]').send_keys(name)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.run.region"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(location)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.run.executionTimeMs"][name="executionTimeMs"]').send_keys(executionTime)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.run.egress"][name="egress"]').send_keys(dataRequest)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.run.requestCount"][name="requestCount"]').send_keys(requestNum)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
