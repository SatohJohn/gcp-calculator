import time
from selenium.webdriver.common.by import By

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        zone = str(row[0].value)
        queries = str(row[1].value)

        function_root_selector = 'form[name="CloudDnsForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudDns.zone"][name="zone"]').send_keys(zone)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudDns.queries"][name="queries"]').send_keys(queries)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
