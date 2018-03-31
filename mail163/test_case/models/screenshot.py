from selenium import webdriver
import os
import time

def screenShot(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))   #
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + file_name  # 注意后面需要多一个斜杠
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('https://mail.163.com')
    #time.sleep(3)
    filename = time.strftime('%Y-%m-%d-%H-%M-%S')+ '-163mail.png'
    screenShot(driver, filename)
    driver.quit()
