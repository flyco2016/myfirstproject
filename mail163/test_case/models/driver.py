from selenium.webdriver import Remote
from selenium import  webdriver
from time import sleep

def broswer():
    driver = webdriver.Chrome()
    # host = 'host:4444'  # 运行用例的主机
    # dc = {'broswerName': 'Chrome'}  # 指定浏览器
    # driver = Remote(command_executor='http://'+host+'/wd/hub',
    #                 desired_capabilities=dc)
    return driver

if __name__ == '__main__':
    dr = broswer()
    dr.get('https://mail.163.com')
    dr.maximize_window()
    sleep(3)
    dr.quit()


