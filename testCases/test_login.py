from pageObjects.loginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_homepageTitle(self, setup):
        self.logger.info('************************Test_001_Login************************')
        self.logger.info('**********************test_homepageTitle**********************')
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.save_screenshot(".\\Screenshots\\" + 'test_homepageTitle.png')
        self.driver.close()
        if actual_title == 'Your store. Login':
            self.logger.info('*********************Testcase passed*********************')
            assert True
        else:
            self.logger.error('*********************Testcase failed*********************')
            assert False

    def test_login(self, setup):
        self.logger.info('************************Test_001_Login************************')
        self.logger.info('**************************test_login**************************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loginpage_obj = Login(self.driver)
        self.loginpage_obj.setUserName(self.username)
        self.loginpage_obj.setPassword(self.password)
        self.loginpage_obj.clickLogin()
        actual_title = self.driver.title
        self.driver.save_screenshot(".\\Screenshots\\" + 'test_login.png')
        self.driver.close()
        if actual_title == 'Dashboard / nopCommerce administration':
            self.logger.info('*********************Testcase passed*********************')
            assert True
        else:
            self.logger.error('*********************Testcase failed*********************')
            assert False
