import time
from selenium.webdriver.common.by import By

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        data = str(row[0].value)
        cachedRequest = str(row[1].value)
        uncachedRequest = str(row[2].value)

        function_root_selector = 'form[name="CloudCdnForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudCdn.cacheEgressApac.value"][name="cacheEgressApac"]').send_keys(data)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudCdn.cacheLookupCount"][name="cacheLookupCount"]').send_keys(cachedRequest)
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.cloudCdn.cacheInvalidationCount"][name="cacheInvalidationCount"]').send_keys(uncachedRequest)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
