from selenium import webdriver
from time import sleep
from pompages.loginpage import LoginPage
#from page.loginpage import LoginPage
import pytest
import unittest
from basepackage import genricsxl
from pompages.searchpage import SearchPage

@pytest.mark.usefixtures('prePostMethod')
class TestDemo(unittest.TestCase):
    #file_path1="C://Users//Umesh//Desktop//test.xlsx‪"
    file_path="E://precondition//testdatadriven.xlsx"
    #file_path="C:\\Users\\admin\\Desktop\\testdata.xlsx"
    pagename="Sheet1"

    @pytest.fixture(autouse=True)
    def classObj(self,prePostMethod):
        # create object for LopginPage class
        self.lp = LoginPage(self.driver)
        self.sp = SearchPage(self.driver)

    # def testValidLogin(self):
    #     username=genricsxl.readData(self.file_path,self.pagename,0,0)
    #     password=genricsxl.readData(self.file_path,self.pagename,0,1)
    #     self.lp.loginTest(username,password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin(self):
    #     username = genricsxl.readData(self.file_path,self.pagename,1,0)
    #     password = genricsxl.readData(self.file_path,self.pagename,1,1)
    #     self.lp.loginTest(username,password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin1(self):
    #     username = genricsxl.readData(self.file_path, self.pagename, 2, 0)
    #     password = genricsxl.readData(self.file_path, self.pagename, 2, 1)
    #     self.lp.loginTest(username, password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin2(self):
    #     username = genricsxl.readData(self.file_path,self.pagename,3,0)
    #     password = genricsxl.readData(self.file_path,self.pagename,3,1)
    #     self.lp.loginTest(username,password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin3(self):
    #     username = genricsxl.readData(self.file_path,self.pagename,4,0)
    #     password = genricsxl.readData(self.file_path,self.pagename,4,1)
    #     self.lp.loginTest(username,password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin4(self):
    #     username = genricsxl.readData(self.file_path,self.pagename,5,0)
    #     password = genricsxl.readData(self.file_path,self.pagename,5,1)
    #     self.lp.loginTest(username,password)
    #     self.lp.verifyLogin()
    #     sleep(3)
    #
    # def testInvalidLogin5(self):
    #     username = genricsxl.readData(self.file_path, self.pagename, 6, 0)
    #     password = genricsxl.readData(self.file_path, self.pagename, 6, 1)
    #     self.lp.loginTest(username, password)
    #     self.lp.verifyLogin()
    #     sleep(3)


    def testlocation(self):
        username = genricsxl.readData(self.file_path, self.pagename, 0, 0)
        password = genricsxl.readData(self.file_path, self.pagename, 0, 1)
        self.lp.loginTest(username, password)
        self.lp.verifyLogin()
        sleep(10)
        self.sp.locationdropdown("Sydney")

    def testselecthotel(self):
        sleep(20)

        self.sp.hotelsdropdown("Hotel Cornice")

    def testselectroomtype(self):
        sleep(20)
        self.sp.roomtypedropdown("Deluxe")

    def testnumberofrooms(self):
        sleep(20)
        self.sp.numberofroomsdropdown("2")

    def testadultsroom(self):
        sleep(20)
        self.sp.AdultsPerRoom_filed("One")

    def testchildroom(self):
        sleep(20)
        self.sp.ChildernPerRoom_filed("Two")
