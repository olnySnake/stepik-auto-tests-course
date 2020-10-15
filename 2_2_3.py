from selenium import webdriver
import time

def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    try:
        browser.get("http://suninjuly.github.io/selects1.html")
        res = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
        browser.find_element_by_id("dropdown").click()
        browser.find_element_by_css_selector("[value='" + str(res) + "']").click()
        browser.find_element_by_xpath("//button[text()='Submit']").click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()