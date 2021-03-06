import time
from selenium.webdriver.common.by import By

def load(driver, sheet):
    for i in range(sheet.nrows)[1:]:
        row = sheet.row(i)
        data = str(row[0].value)

        function_root_selector = 'form[name="SpeechApiForm"]'
        driver.find_element(By.CSS_SELECTOR, function_root_selector + ' ' + '[ng-model="listingCtrl.speechApi.recognition"][name="recognition"]').send_keys(data)

        time.sleep(0.1)
        element = driver.find_element(By.CSS_SELECTOR, function_root_selector)
        element.submit()
