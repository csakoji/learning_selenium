class Login:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    checkbox_rememberme_id = 'RememberMe'
    button_login_xpath = '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input'
    link_logout_linktext = 'Logout'

    def __init__(self, driver):
        self.driver = driver

    # Login page testcases are data driven testcases
    def setUserName(self, username):
        # Clear text field so that previous testcases data should not cause problem
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        # Clear text field so that previous testcases data should not cause problem
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()




