from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
import time, os
from test163mailpro.mail163.test_case.models import sendemail

def find_newest_report(testreport):
    """
	为了验证自动触发构建而添加，再次添加
	"""
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+'\\'+fn))
    newest_report = os.path.join(testreport, lists[-1])
    print(newest_report)
    return newest_report

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = './mail163/report/HTMLReport/' + now + '-result.html'
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream=f,
                                title='163邮箱自动化测试报告',
                                description='''
                                      测试环境：windows 7
                                      浏览器：Chrome
                                      '''
                                )
        discover = unittest.defaultTestLoader.discover('./mail163/test_case/testcases/', pattern='*_sta.py')
        runner.run(discover)

    file_path = find_newest_report('./mail163/report/HTMLReport/')
    sendemail.send_email(file_path)
