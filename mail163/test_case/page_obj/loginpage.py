#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from .basepage import Page
from time import sleep
from selenium import webdriver

class LoginPage(Page):
    '''
    创建邮箱登录对象类
    '''
    #
    # bbs_move_to_loc = (By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/div/div[3]/div/div/div[1]/img')
    # bbs_login_button_loc = (By.XPATH, '//*[@id="mzLogin"]')
    # 打开登录界面
    # def open_login_page(self):
    #     elem_1 = self.find_element(*self.bbs_move_to_loc)
    #     ActionChains(self.driver).move_to_element(elem_1).perform()
    #     elem_2 = self.driver.find_element(*self.bbs_login_button_loc)
    #     elem_2.click()

    # 定义一些变量并且赋值
    url = '/'
    login_username_loc = (By.NAME, 'email')
    login_password_loc = (By.NAME, 'password')
    login_button_loc = (By.ID, 'dologin')

    # 切换iframe，为了能够定位到元素
    def switch_frame(self):
        sleep(3)
        self.driver.switch_to.frame('x-URS-iframe')

    # 输入登录用户
    def input_login_username(self, username):
        elem = self.find_element(*self.login_username_loc)
        elem.clear()
        elem.send_keys(username)

    # 输入密码
    def input_login_password(self, password, wantToEmpty=False):
        elem = self.find_element(*self.login_password_loc)
        elem.clear()
        elem.send_keys(password)
        if wantToEmpty:
            elem.clear()

    def click_login_button(self):
        self.find_element(*self.login_button_loc).click()

    # 定义统一登录入口
    def user_login(self, username=17727820013, password='mtf114255', wantToPasswdEmp=False):
        self.open()
        self.switch_frame()
        self.input_login_username(username)
        self.input_login_password(password, wantToEmpty=wantToPasswdEmp)
        self.click_login_button()

    # 处理各类登录后的提示
    # 用户登录成功
    def user_login_success_hint(self):
        sleep(5)
        return self.driver.find_element_by_css_selector('#_mail_component_41_41 > a').text

    # 账号为空的提示
    # 密码为空的提示
    # 账号密码不为空但是不对的提示
    def user_login_fail_hint(self):
        return self.driver.find_element_by_class_name('ferrorhead').text

if __name__ == "__main__":
    instPageLogin = LoginPage(webdriver.Chrome())

    #登录成功的提示
    instPageLogin.user_login()
    print(instPageLogin.user_login_success_hint())
    instPageLogin.quitBroswer()

    # # 账号为空的提示
    # instPageLogin.user_login(username='', password=123344)
    # sleep(3)
    # print(instPageLogin.user_login_fail_hint())

    # # 密码为空的提示
    # instPageLogin.user_login(username=17727820013, wantToPasswdEmp=0)
    # sleep(3)
    # print(instPageLogin.user_login_fail_hint())

    # # 账号和密码不对的提示
    # instPageLogin.user_login(username=17727820013, password=123345344)
    # sleep(3)
    # print(instPageLogin.user_login_fail_hint())







