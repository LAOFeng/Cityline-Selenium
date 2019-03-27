from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def login(un,pw):
    driver.get("https://www.cityline.com/Login.do?targetUrl=https%3A%2F%2Fwww.cityline.com%2FEvents.do")
    try:
        WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_name("submit"))
        elem = driver.find_element_by_name("username")
        elem.send_keys(un)
        elem = driver.find_element_by_name("password")
        elem.send_keys(pw)
        elem = driver.find_element_by_name("submit")
        elem.click()   
        WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id("headerUsername")) 
    except:
        driver.refresh()
    
def RunQP(MaydayWeb):
    driver.get(MaydayWeb)
    time.sleep(1)
    if (driver.current_url=='http://msg.cityline.com/busy.html'):
        driver.get(MaydayWeb)
    else:
        time.sleep(100000)
    
    
'''
time.sleep(5)
    driver.implicitly_wait(5)
    driver.get(MaydayWeb)
    WebDriverWait(driver,100).until(lambda driver:driver.find_element_by_id("buyBt"))
    driver.execute_script("javascript:selectPerformance(0);")
    time.sleep(100)
'''
    #	系統偵測到以下問題 :
#-閣下的戶口已被登入;或
#-閣下上一次未能成功登出 

#請注意：如重新登入，上述情況所預留的座位將不再保留。要繼續 ? 
#http://msg.cityline.com/busy.html

if __name__=='__main__':
    MaydayWeb="http://event.cityline.com/utsvInternet/internet/action/event.do?actionFwd=eventDetail&event=29920&actionType=5&lang=TW"
    un = "liaozefeng@hotmail.com"
    pw = "LZF24685"
    desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
    desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    driver = webdriver.Chrome()
    login(un,pw)
    RunQP(MaydayWeb)







