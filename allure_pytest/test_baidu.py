from time import sleep

import allure
import pytest
from selenium import webdriver


@allure.testcase("http://github.com","测试用例管理")#连接到测试用例管理的一个网页
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data',['allure','pytest','unittest'])
def test_steps_demo(test_data):

    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com/")

    with allure.step(f"输入搜索词:{'test_data'}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        sleep(2)
        driver.find_element_by_id("su").click()
        sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png",attachment_type=allure.attachment_type.PNG)
    with allure.step("关闭浏览器"):
        driver.quit()



