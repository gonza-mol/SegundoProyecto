from selenium.webdriver.common.by import By

class LoginPageLocators():
    txt_username = (By.ID, "loginFrm_loginname")
    txt_password = (By.ID, "loginFrm_password")
    btn_sign_in = (By.CSS_SELECTOR, "#loginFrm>fieldset>button")
    label_incorrect_username = (By.CSS_SELECTOR, "#maincontainer>div>div>div>div.alert.alert-error.alert-danger")
    check_box_register = (By.ID, "accountFrm_accountregister")
    btn_continue_register1 = (By.CSS_SELECTOR, ".btn.btn-orange.pull-right:nth-child(3)")





class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def submit_Username(self, username):
        self.driver.find_element(*LoginPageLocators.txt_username).send_keys(username)

    def submit_Password(self, password):
        self.driver.find_element(*LoginPageLocators.txt_password).send_keys(password)

    def click_Submit_Sign_In(self):
        self.driver.find_element(*LoginPageLocators.btn_sign_in).click()

    def click_Register_Account(self):
        self.driver.find_element(*LoginPageLocators.check_box_register).click()

    def click_Continue_Registration(self):
        self.driver.find_element(*LoginPageLocators.btn_continue_register1).click()

    def show_error_username_password(self):
        return self.driver.find_element(*LoginPageLocators.label_incorrect_username).text

    def verify_IsChecked(self):
        return self.driver.find_element(*LoginPageLocators.check_box_register).is_selected()

    def submit_Continue(self):
        self.driver.find_element(*LoginPageLocators.btn_continue_register1).click()



