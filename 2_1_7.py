from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  
def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    try:
        browser.get("http://suninjuly.github.io/get_attribute.html")
        res = calc(browser.find_element_by_id("treasure").get_attribute("valuex"))
        browser.find_element_by_id("answer").send_keys(res)
        browser.find_element_by_id("robotCheckbox").click()
        browser.find_element_by_id("robotsRule").click()
        browser.find_element_by_xpath("//button[text()='Submit']").click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()