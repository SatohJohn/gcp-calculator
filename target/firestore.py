import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        location = 'asia-northeast1'
        read = str(row[0].value)
        write = str(row[1].value)
        delete = str(row[2].value)
        storage = str(row[3].value)

        function_root_selector = 'form[name="FirestoreForm"]'

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.firestore.location"]').click()
        time.sleep(0.1)
        driver.find_element(By.CSS_SELECTOR, 'body > div[aria-hidden="false"] > md-select-menu md-option[value="{}"]'.format(location)).click()

        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.firestore.documentReadsCount"][name="documentReadsCount"]').send_keys(read)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.firestore.documentWritesCount"][name="documentWritesCount"]').send_keys(write)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.firestore.documentDeletesCount"][name="documentDeletesCount"]').send_keys(delete)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.firestore.storedDataVolume.value"][name="storedDataVolume"]').send_keys(storage)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
