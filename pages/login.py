from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait


class Login_page:    #Used to navigate to Login Page
    log=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    def __init__(self,driver):
        self.driver=driver
    def click_log(self):
        self.driver.find_element(*self.log).click()
        wait(self.driver,10).until(EC.url_contains("/login"))

class Details_user:  #Used to enter user details and login
    mail=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[2]')  #here we used XPATH Locator because in website we are having 2 input fields with same name "email" 
    password=(By.NAME,"password")
    def __init__(self,driver):
        self.driver=driver
    def enter_email(self,usermail):
        self.driver.find_element(*self.mail).send_keys(usermail)
    def enter_password(self,pwd):
        self.driver.find_element(*self.password).send_keys(pwd)
    def click_login(self):
        self.driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/button').click()

class View_cart:
    cart=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    def __init__(self,driver):
        self.driver=driver
    def click_cart(self):
        self.driver.find_element(*self.cart).click()
        wait(self.driver,10).until(EC.url_contains("/view_cart"))
