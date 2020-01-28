import time
from selenium.webdriver.common.by import By

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        message = str(row[0].value)
        retained = str(row[1].value)
        snapshot = str(row[2].value)

        function_root_selector = 'form[name="PubSubForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.pubSub.operations.value"][name="operations"]').send_keys(message)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.pubSub.retainedVolume.value"][name="retainedVolume"]').send_keys(retained)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.pubSub.snapshotVolume.value"][name="snapshotVolume"]').send_keys(snapshot)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()

