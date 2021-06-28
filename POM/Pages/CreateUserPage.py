from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class CreateUserPageLocators():

    label_first_name = (By.ID, "AccountFrm_firstname")
    label_last_name = (By.ID, "AccountFrm_lastname")
    label_email = (By.ID, "AccountFrm_email")
    label_address_1 = (By.ID, "AccountFrm_address_1")
    label_city = (By.ID, "AccountFrm_city")
    drop_down_region = (By.ID, "AccountFrm_zone_id")
    label_zip_code = (By.ID, "AccountFrm_postcode")
    drop_down_country = (By.ID, "AccountFrm_country_id")
    label_create_user_name = (By.ID, "AccountFrm_loginname")
    label_create_password = (By.ID, "AccountFrm_password")
    label_confirm_password = (By.ID, "AccountFrm_confirm")
    check_box_suscribe = (By.ID, "AccountFrm_newsletter0")
    check_box_policy = (By.ID, "AccountFrm_agree")
    btn_continue_register2 = (By.CSS_SELECTOR, "#AccountFrm>div.form-group>div>div>button")
    btn_continue_register3 = (By.CSS_SELECTOR, "#maincontainer>div>div.col-md-9.col-xs-12.mt20>div>div>section>a")



class CreateUserPage():

    def __init__(self, driver):
        self.driver = driver

    def create_First_Name(self, firstname):
        self.driver.find_element(*CreateUserPageLocators.label_first_name).send_keys(firstname)

    def create_Last_Name(self, lastname):
        self.driver.find_element(*CreateUserPageLocators.label_last_name).send_keys(lastname)

    def create_Email(self, email):
        self.driver.find_element(*CreateUserPageLocators.label_email).send_keys(email)

    def create_Address1(self, address):
        self.driver.find_element(*CreateUserPageLocators.label_address_1).send_keys(address)

    def create_City(self, city):
        self.driver.find_element(*CreateUserPageLocators.label_city).send_keys(city)

    def create_Country(self, country):
        sel = Select(self.driver.find_element(*CreateUserPageLocators.drop_down_country))
        sel.select_by_visible_text(country)

    def create_Region(self, region):
        sel = Select(self.driver.find_element(*CreateUserPageLocators.drop_down_region))
        sel.select_by_visible_text(region)


    def create_Zip_Code(self, country):
        self.driver.find_element(*CreateUserPageLocators.label_zip_code).send_keys(country)

    def create_Login_Name(self, login_name):
        self.driver.find_element(*CreateUserPageLocators.label_create_user_name).send_keys(login_name)

    def create_Create_Password(self, create_pass):
        self.driver.find_element(*CreateUserPageLocators.label_create_password).send_keys(create_pass)

    def create_Confirm_Password(self, confirm_pass):
        self.driver.find_element(*CreateUserPageLocators.label_confirm_password).send_keys(confirm_pass)

    def create_Suscribe(self):
        self.driver.find_element(*CreateUserPageLocators.check_box_suscribe).click()

    def create_Policy(self):
        self.driver.find_element(*CreateUserPageLocators.check_box_policy).click()




