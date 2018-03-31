from time import sleep
import unittest, random, sys
#sys.path.append('./models')
#sys.path.append('./page_obj')
from test163mailpro.mail163.test_case.models import myunit, screenshot
from test163mailpro.mail163.test_case.page_obj.loginpage import LoginPage

class LoginTest(myunit.MyTest):
    '''
    邮箱登录测试
    '''
    def user_login_verify(self, username='', password=''):
        LoginPage(self.driver).user_login(username, password)

    def test_login1(self):
        '''
        验证登录成功
        '''
        self.user_login_verify(username=17727820013, password='mtf114255')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_login_success_hint(),  '退出')
        screenshot.screenShot(self.driver, 'login_success.png')

    def test_login2(self):
        '''
        验证账号为空，无法登录，提示：请输入账号
        '''
        self.user_login_verify(username='', password='mtf114255')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_login_fail_hint(), '请输入帐号')
        screenshot.screenShot(self.driver, 'login_fail_empty_username.png')

    def test_login3(self):
        '''
        验证密码为空，无法登录，提示：请输入密码
        '''
        self.user_login_verify(username=17727820013, password='')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_login_fail_hint(), '请输入密码')
        screenshot.screenShot(self.driver, 'login_fail_empty_password.png')

    def test_login4(self):
        '''
        验证账号密码不匹配，无法登录，提示：账号或密码错误
        '''
        self.user_login_verify(username=17727820013, password='mtf1142556')
        po = LoginPage(self.driver)
        self.assertEqual(po.user_login_fail_hint(), '帐号或密码错误')
        screenshot.screenShot(self.driver, 'login_fail_username_and_password_notmatch.png')


if __name__ == '__main__':
    unittest.main(verbosity=2)
