#coding=utf-8
from appium import webdriver
import time,os,re
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android001'
desired_caps['unicodeKeyboard'] = True
desired_caps["resetKeyboard"] = True
desired_caps["newCommandTimeout"]=30
desired_caps['fullReset'] = 'false'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
desired_caps['recreateChromeDriverSessions'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 10
desired_caps['chromeOptions']={'androidProcess': 'com.tencent.mm:appbrand0'}
driver = webdriver.Remote(command_executor = 'http://127.0.0.1:4723/wd/hub',desired_capabilities = desired_caps)
time.sleep(2)
time.sleep(1)
driver.implicitly_wait(10)
driver.find_element_by_name('发现').click()
time.sleep(1)
driver.swipe(100,1200,100,900)
driver.find_element_by_name('小程序').click()
driver.find_element_by_name('美团外卖').click()
time.sleep(2)
contexts = driver.contexts
print contexts
time.sleep(2)
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
print '切换成功'
print driver.current_context
all_handles = driver.window_handles
print len(all_handles)
for handle in all_handles:
    try:
        driver.switch_to_window(handle)
        print driver.page_source
        driver.find_element_by_css_selector('.filter-select.flex-center')    #定位“筛选 ”按钮
        print '定位成功'
        break
    except Exception as e:
        print e
driver.find_element_by_css_selector('.filter-select.flex-center').click()
time.sleep(5)
driver.quit()