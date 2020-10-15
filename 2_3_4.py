from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    try:
        browser.get("http://suninjuly.github.io/alert_accept.html")
        browser.find_element_by_tag_name("button").click()
        browser.switch_to.alert.accept()
        res = calc(browser.find_element_by_id("input_value").text)
        browser.find_element_by_id("answer").send_keys(str(res))
        browser.find_element_by_xpath("//button[text()='Submit']").click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()