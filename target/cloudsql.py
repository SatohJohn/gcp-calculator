import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        num = str(1)
        instance = 'db-n1-standard-1'
        location = 'asia-northeast1'
        storage = str(10.0)
        if (row[0].value > 10.0):
            storage = str(row[0].value)
        backup = str(row[1].value)

        function_root_selector = 'form[name="CloudSQLForm2"]'

        elements = driver.find_elements(By.CSS_SELECTOR, 'md-pagination-wrapper md-tab-item')
        for e in elements:
            if ('Second Generation'.upper() in e.text.upper()):
                e.click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.instanceCount"][name="instanceCount"]').send_keys(num)

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.instance"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(instance)).click()
        time.sleep(0.1)

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.includeHA"]').click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.location"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(location)).click()
        time.sleep(0.1)

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.storage.value"][name="storage"]').send_keys(storage)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudSQL2.backup.value"][name="backup"]').send_keys(backup)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
