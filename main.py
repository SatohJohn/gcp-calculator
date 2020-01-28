import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xlrd
import openpyxl
import pprint
import sys

args = sys.argv
from target import functions
from target import gce
from target import networks
from target import bigquery
from target import cloudsql
from target import firestore
from target import pubsub
from target import dns
from target import cdn
from target import speech
from target import cloudrun

def selectService(driver, serviceName):
    serviceFinder = driver.find_element(By.ID, 'input-0')
    serviceFinder.send_keys(serviceName)
    time.sleep(0.1)
    suggestion = driver.find_element(By.CSS_SELECTOR, 'ul.md-autocomplete-suggestions > li')
    suggestion.click()
    serviceFinder.clear()
    time.sleep(0.1)

driver = webdriver.Chrome()
driver.implicitly_wait(2)

if (len(sys.argv) != 2):
    print('引数 1つを渡してください')
    print('第1引数は excelファイルの有るパスです')
    sys.exit(1)

fileName = sys.argv[1]
url = 'https://cloudpricingcalculator.appspot.com/'
driver.get(url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'input-0')))

wb = xlrd.open_workbook(fileName)

for sheet in wb.sheets():
    if sheet.name.upper() == 'functions'.upper():
        selectService(driver, 'Cloud Functions')
        functions.load(driver, sheet)
    if sheet.name.upper() == 'GCE'.upper():
        selectService(driver, 'Compute Engine')
        gce.load(driver, sheet)
    if sheet.name.upper() == 'network'.upper():
        selectService(driver, 'Networking')
        networks.load(driver, sheet)
    if sheet.name.upper() == 'BigQuery'.upper():
        selectService(driver, 'BigQuery')
        bigquery.load(driver, sheet)
    if sheet.name.upper() == 'sql'.upper():
        selectService(driver, 'Cloud SQL')
        cloudsql.load(driver, sheet)
    if sheet.name.upper() == 'firestore'.upper():
        selectService(driver, 'Cloud Firestore')
        firestore.load(driver, sheet)
    if sheet.name.upper() == 'pubsub'.upper():
        selectService(driver, 'Cloud Pub/Sub')
        pubsub.load(driver, sheet)
    if sheet.name.upper() == 'dns'.upper():
        selectService(driver, 'Cloud Dns')
        dns.load(driver, sheet)
    if sheet.name.upper() == 'cdn'.upper():
        selectService(driver, 'Cloud CDN')
        cdn.load(driver, sheet)
    if sheet.name.upper() == 'speech'.upper():
        selectService(driver, 'Speech API')
        speech.load(driver, sheet)
    if sheet.name.upper() == 'cloudRun'.upper():
        selectService(driver, 'Cloud Run')
        cloudrun.load(driver, sheet)

time.sleep(0.1)

print('usd')
print(driver.find_element(By.CSS_SELECTOR, 'h2.md-title > b').text)
print(driver.current_url)

print('jpy')
driver.find_element(By.CSS_SELECTOR, 'md-select[ng-model="appCtrl.currency"]').click()
time.sleep(0.1)
driver.find_element(By.CSS_SELECTOR, 'md-content > md-option[value="JPY"]').click()
print(driver.find_element(By.CSS_SELECTOR, 'h2.md-title > b').text)
print(driver.current_url)

driver.quit()
