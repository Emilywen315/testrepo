# -*- coding: utf-8 -*-
from appium import webdriver


import time

desired_caps = {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'M9N7N15930001618',
                'appPackage': 'com.tencent.mm',
                'appActivity': 'com.tencent.mm.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                'unicodeKeyboard': True,
                'resetKeyboard': True,
                'noReset': True,
                'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
                }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


# 点微信首页lexus
driver.find_element_by_xpath(".//android.view.View[@text='lexus']").click()
# 点击二手车
time.sleep(3)
driver.find_element_by_xpath(".//android.view.View[@text='二手车']").click()
# 点击提交线索
time.sleep(3)
driver.find_element_by_xpath(".//android.widget.TextView[@text='提交线索']").click()

"""
Sleep(5) 
#获取当前上下文
c=driver.contexts
print(c)
#输出结果['NATIVE_APP', 'WEBVIEW_com.tencent.mm:tools']
#切换为 webview，名称就是从上面的语句得来的
driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')

#输入车架号
time.sleep(3)
driver.find_element_by_xpath('.//*[@id="app"]/article/section/div[1]/div/div[1]/div[2]/input').clear()
driver.find_element_by_xpath('.//*[@id="app"]/article/section/div[1]/div/div[1]/div[2]/input').send_keys("WGYA1245678765139")
sleep(10)
"""