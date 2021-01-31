from selenium.webdriver.support.ui import Select


class AddCustomer:

    menu_customers_xpath = '/html/body/div[3]/div[2]/div/ul/li[4]/a/span'
    submenu_customers_xpath = '/html/body/div[3]/div[2]/div/ul/li[4]/ul/li[1]/a'
    button_add_cust = '/html/body/div[3]/div[3]/div/form[1]/div[1]/div/a'
    textbox_addcust_email_id = 'Email'
    textbox_addcust_password_id = 'Password'
    textbox_addcust_firstName_id = 'FirstName'
    textbox_addcust_lastName_id = 'LastName'
    radiobutton_addcust_maleGender_id = 'Gender_Male'
    radiobutton_addcust_femaleGender_id = 'Gender_Female'
    textbox_addcust_date_id = 'DateOfBirth'
    textbox_addcust_company_id = 'Company'
    checkbox_addcust_tax_id = 'IsTaxExempt'
    textbox_addcust_newsletter_xpath = '//*[@id="customer-info"]/div[2]/div[1]/div[9]/div[2]/div/div[1]'
    textbox_addcust_custrole_xpath = '//*[@id="customer-info"]/div[2]/div[1]/div[10]/div[2]/div/div[1]/div'
    custrole_guests_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[1]'
    custrole_registered_xpath = '//*[@id="SelectedCustomerRoleIds_taglist"]/li[2]/span[1]'
    drpdwn_addcust_managerofvender_xpath = '//*[@id="VendorId"]'
    checkbox_addcust_active_id = 'Active'
    button_addcust_save_xpath = '/html/body/div[3]/div[3]/div/form/div[1]/div/button[1]'

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.menu_customers_xpath).click()

    def clickOnCustomersSubmenu(self):
        self.driver.find_element_by_xpath(self.submenu_customers_xpath).click()

    def clickAddCust(self):
        self.driver.find_element_by_xpath(self.button_add_cust).click()

    def setEmail(self, email):
        self.driver.find_element_by_id(self.textbox_addcust_email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_addcust_password_id).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.textbox_addcust_firstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.textbox_addcust_lastName_id).send_keys(lname)

    def selectGenderMale(self):
        self.driver.find_element_by_id(self.radiobutton_addcust_maleGender_id).click()

    def selectGenderFemale(self):
        self.driver.find_element_by_id(self.radiobutton_addcust_femaleGender_id).click()

    def setDOB(self, date):
        self.driver.find_element_by_id(self.textbox_addcust_date_id).send_keys(date)

    def setCompany(self, company):
        self.driver.find_element_by_id(self.textbox_addcust_company_id).send_keys(company)

    def setTaxExempt(self):
        self.driver.find_element_by_id(self.checkbox_addcust_tax_id).click()

    def setNewsLetter(self, newsletter):
        self.driver.find_element_by_xpath(self.textbox_addcust_newsletter_xpath).send_keys(newsletter)

    def setCustomerRoles(self, custrole):
        self.driver.find_element_by_xpath(self.textbox_addcust_custrole_xpath).click()
        if custrole.lower() == 'guets':
            self.driver.find_element_by_xpath(self.custrole_guests_xpath).click()
        elif custrole.lower() == 'registered':
            self.driver.find_element_by_xpath(self.custrole_registered_xpath).click()

    def setManagerOfVender(self, vendor):
        element = self.driver.find_element_by_xpath(self.drpdwn_addcust_managerofvender_xpath)
        drp = Select(element)
        drp.select_by_visible_text(vendor)

    def clickSave(self):
        self.driver.find_element_by_xpath(self.button_addcust_save_xpath).click()
