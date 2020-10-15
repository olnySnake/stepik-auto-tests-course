from selenium import webdriver
import time
import os

def main():
    browser = webdriver.Chrome('C:\\Users\\Snake\\python-scripts\\gec_for_selenium\\chromedriver\\chromedriver.exe')
    try:
        browser.get("http://suninjuly.github.io/file_input.html")  
        browser.find_element_by_xpath("//input[@name='firstname']").send_keys("firstname")
        browser.find_element_by_xpath("//input[@name='lastname']").send_keys("lastname")
        browser.find_element_by_xpath("//input[@name='email']").send_keys("email")
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test.txt')
        browser.find_element_by_xpath("//input[@name='file']").send_keys(file_path)
        browser.find_element_by_xpath("//button[text()='Submit']").click()
    finally:
        time.sleep(10)
        browser.quit()

if __name__ == "__main__":
    main()