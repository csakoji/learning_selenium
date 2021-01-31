from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLutils

class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logGen()
    filepath = ".\\TestData\\LoginData.xlsx"
    sheetName = 'Sheet1'

    def test_login(self, setup):
        self.logger.info('************************Test_002_Login************************')
        self.logger.info('**************************test_login**************************')
        self.driver = setup
        rowCount = XLutils.getRowCount(self.filepath, self.sheetName)
        self.driver.get(self.baseURL)
        self.loginpage_obj = Login(self.driver)
        result_list = list()
        for r in range(2, rowCount+1):
            self.username = XLutils.readData(self.filepath, self.sheetName, r, 1)
            self.password = XLutils.readData(self.filepath, self.sheetName, r, 2)
            result = XLutils.readData(self.filepath, self.sheetName, r, 3)
            self.loginpage_obj.setUserName(self.username)
            self.loginpage_obj.setPassword(self.password)
            self.loginpage_obj.clickLogin()
            actual_title = self.driver.title
            expected_title = 'Dashboard / nopCommerce administration'
            if actual_title == expected_title:
                if result == 'pass':
                    self.logger.info("Testcase passed")
                    result_list.append(True)
                else:
                    self.logger.error("Testcase failed")
                    result_list.append(False)
                self.loginpage_obj.clickLogout()
            elif actual_title != expected_title:
                if result != 'pass':
                    self.logger.info("Testcase passed")
                    result_list.append(True)
                else:
                    result_list.append(False)
                    self.logger.error("Testcase failed")

        self.driver.close()
        if all(result_list):
            self.logger.info("All testcases passed")
            assert True
        else:
            self.logger.error("One or all testcases failed")
            assert False

