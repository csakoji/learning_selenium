from pageObjects.loginPage import Login
from pageObjects.addCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from string import ascii_lowercase, digits
import random
import pdb


def create_random_alphnum_data(length=8, chars=ascii_lowercase+digits):
    return ''.join(random.choice(chars) for _ in range(length))


class Test_003_Add_Customer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_add_customer(self, setup):
        self.logger.info("Add customer testcases starts")
        self.logger.info("Login to website")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login to webpage successful")
        self.logger.info('Click on customers menu and submenu and add customer')
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubmenu()
        self.addcust.clickAddCust()
        self.logger.info("Providing new customer information")
        self.email = create_random_alphnum_data() + '@gmail.com'
        self.addcust.setEmail(self.email)
        self.addcust.setPassword('Mypassword')
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVender("Vendor 2")
        self.addcust.selectGenderMale()
        self.addcust.setFirstName("Pavan")
        self.addcust.setLastName("Kumar")
        self.addcust.setDOB("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompany("busyQA")
        self.addcust.clickSave()
        self.logger.info('Checking if customer added successfully')
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            self.driver.save_screenshot(".\\Screenshots\\" + 'CustomerAddPassed.png')
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + 'CustomerAddFailed.png')
            assert False
        self.logger.info('Closing browser window')
        self.driver.quit()


