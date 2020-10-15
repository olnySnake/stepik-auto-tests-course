from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    try:
        browser.get("http://suninjuly.github.io/execute_script.html")  
        res = calc(browser.find_element_by_id("input_value").text)
        browser.find_element_by_id("answer").send_keys(str(res))
        button = browser.find_element_by_xpath("//button[text()='Submit']")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        browser.find_element_by_id("robotCheckbox").click()
        browser.find_element_by_id("robotsRule").click()
        button.click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()