from selenium import webdriver
from selenium.webdriver.common.keys import Keys


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    print(driver.find_element_by_id("lg"))
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()