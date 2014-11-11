import time
from selenium import webdriver
import unittest
from unittest.case import TestCase
import unittest
from StringIO import StringIO
from pyvirtualdisplay import Display
from selenium import webdriver
class ExampleTestCase(TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(1280, 1024))
        self.display.start()
        self.driver = webdriver.Firefox()




    def test_example(self):
        self.driver.get("http://www.ex.ua/ru/video/foreign_series")
        time.sleep(5)
        elem = self.driver.find_elements_by_css_selector("html body table tbody tr td#body_element table.include_0 tbody tr td p a b")
        a=0
        filelog =  open("log.txt", "w")
        for i in elem:
            a = a+1
            print(str(a)+" "+i.text+"/n")
            #filelog.write(str(a)+" "+i.text+"/n")
        filelog.close()


    def tearDown(self):
        self.driver.quit()
        self.display.stop()


if __name__ == "__main__":
    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(unittest.makeSuite(ExampleTestCase))
    print(runner)
    print(result)
    unittest.main()



