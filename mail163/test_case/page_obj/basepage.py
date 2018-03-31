from selenium import webdriver
from time import sleep

class Page:
    '''
    页面对象基础类，用于所有页面类的继承
    '''
    mail_url = 'https://mail.163.com'

    def __init__(self, selenium_driver, base_url=mail_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    """
    1.带有单下划线的特性不会被from module import *导入
    2.单下划线是Python程序员使用类时的约定，表明程序员不希望类的用户直接访问属性。仅仅是一种约定！
    实际上，实例._变量，可以被访问。
    """
    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def run_script(self, src):
        return self.driver.execute_script(src)

    def quitBroswer(self):
        return self.driver.quit()

    def closeWindow(self):
        return self.driver.close()

    def __test_fake_var(self):
        pass


if __name__ == '__main__':
    pageinst = Page(webdriver.Chrome())
    pageinst._Page__test_fake_var()   # 通过添加_page来访问， 可以减少命名冲突
    pageinst.url = '/'   # 在外面定义属性，这个可以在下面的继承类中实现
    pageinst._open(pageinst.url)
    print(pageinst.on_page())
    sleep(3)
    print(pageinst.run_script('document.title'))
    pageinst.driver.quit()





