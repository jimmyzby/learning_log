from selenium import webdriver
import time
import pytest
import allure


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data', ['python', 'unittest', 'pytest'])
def test_demo(test_data):
    with allure.step("打开百度"):
        chrome_opt = webdriver.ChromeOptions()
        chrome_opt.add_argument('--disable-gpu')
        driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_opt)
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step("输入搜索词"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)

        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file('./result/b.png', attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()
