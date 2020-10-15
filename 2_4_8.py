from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    browser.implicitly_wait(5)
    try:
        browser.get("http://suninjuly.github.io/explicit_wait2.html")
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
        browser.find_element_by_xpath("//button[text()='Book']").click()
        res = calc(browser.find_element_by_id("input_value").text)
        browser.find_element_by_id("answer").send_keys(str(res))
        browser.find_element_by_xpath("//button[text()='Submit']").click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()