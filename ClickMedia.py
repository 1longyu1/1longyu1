# coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *



def MedEvaluate():
    temp = 1
    for i in range(1, 90):
        temp = temp + 1
        myKeys = 0
        findEvaluate = 0
        try:
            mySelector_evaluate = "#showajaxinfo > div:nth-child(2) > dl > dd > p:nth-child(%d)" % i
            evaluate = driver.find_element(By.CSS_SELECTOR,mySelector_evaluate)
            # 利用css定位元素 媒体评价
        except NoSuchElementException:
            print("这个不用评")
        #    findEvaluate = findEvaluate + 1
        # if findEvaluate == 2:
        #    break
        try:
            driver.execute_script("arguments[0].click();", evaluate)
            # 利用script点击按钮，可以防止元素未出现在界面中而不能点击出现异常
            evaluate = driver.switch_to.frame("pageiframe")  # 转换到媒体评价的iframe
            evaluate = driver.find_element(By.CSS_SELECTOR,"ping_btn_3").click()  # 点击“很好”评价
            time.sleep(1)
            evaluate = driver.find_element(By.CSS_SELECTOR,"aui_state_highlight").click()  # 点击确定评价
            evaluate = driver.switch_to.default_content()  # 回到主界面不用点击关闭按钮就可以直接定位主界面的元素
            myKeys = 1
        except:
            print("进行下一个评价")
            if myKeys == 0:
                evaluate = driver.switch_to.default_content()
        else:
            print("进行下一个评价")
        print(temp)
        # 最开始是2034
        # j_2046 > a
        # j_2045 > a

if __name__ == '__main__':
    username = "*****"
    pwd = "*****"
    driver = webdriver.Chrome()
    driver.get('http://www.attop.com/user/study.htm')
    alert = driver.switch_to.frame("pageiframe")
    time.sleep(1)  # 转化到登录界面的iframe
    input_username = driver.find_element(By.ID, "username").send_keys(username)
    input_password = driver.find_element(By.ID, "password").send_keys(pwd)
    time.sleep(6)  # 等待输入验证码
    find_class = driver.find_element(By.XPATH, '//*[@id="showajaxinfo"]/div/table/tbody/tr[2]/td[6]/a/span').click()
    # 找出新窗口：
    new_window = driver.window_handles[-1]  # '-1'代表打开的最后一个窗口
    # 切换到新窗口：
    driver.switch_to.window(new_window)
    select_title = driver.find_element(By.LINK_TEXT, "课程学习").click()
    time.sleep(2)


    for i in range(2254, 2309):
        flag = 0
        capterKeys = "#j_%d > a" % i
        try:
            clickCapter = driver.find_element(By.CSS_SELECTOR,capterKeys)
            # clickCapter = driver.find_element_by_css_selector(capterKeys)
            driver.execute_script("arguments[0].click();", clickCapter)
        except:
            print("这章没有")
            print(i)
            flag = 1
        if (flag == 0):
            MedEvaluate()
