import time
from selenium.webdriver.common.by import By

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        name = str(row[0].value)
        storage = str(row[1].value)
        streamingInserts = str(row[2].value)
        query = str(row[3].value)
        location = str(row[4].value)

        function_root_selector = 'form[name="BigQueryForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.bigQuery.location"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div > md-select-menu md-option[value="{}"]'.format(location)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.bigQuery.name"][name="name"]').send_keys(name)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.bigQuery.storage.value"][name="storage"]').send_keys(storage)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.bigQuery.streamingInserts.value"][name="streamingInserts"]').send_keys(streamingInserts)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.bigQuery.interactiveQueries.value"][name="interactiveQueries"]').send_keys(query)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
