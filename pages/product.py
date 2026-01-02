from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait

class product_page():
    first_product=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a')
    addProduct=(By.XPATH, "//button[contains(text(),'Add to cart')]")
    
    def __init__(self,driver):
        self.driver=driver

    def navigate_to_product(self):
        self.driver.find_element(*self.first_product).click()

    first_product = (By.XPATH, "//a[@href='/product_details/1']")
    add_to_cart_btn = (By.CSS_SELECTOR, "button.btn.btn-default.cart")
    view_cart_btn = (By.XPATH, "//u[text()='View Cart']")
    viewCart=(By.CSS_SELECTOR,'a[href="/view_cart"]')
    search_product=(By.CSS_SELECTOR,'a[href="/products"]')

    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def navigate_to_product(self):
        self.wait.until(EC.element_to_be_clickable(self.first_product)).click()

    def click_add_to_cart(self):
        # Scroll to Add to Cart
        add_btn = self.wait.until(EC.presence_of_element_located(self.add_to_cart_btn))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_btn)

        # JS click (prevents intercepted error)
        self.driver.execute_script("arguments[0].click();", add_btn)

        # Click View Cart popup
        self.wait.until(EC.element_to_be_clickable(self.view_cart_btn)).click()
        #click view cart
    def click_view_cart(self):
        self.driver.find_element(*self.viewCart).click()
    
        self.wait.until(EC.url_contains("/view_cart"))
    
    def navigate_to_products_page(self,product_name):
        self.driver.find_element(*self.search_product).click()
        self.wait.until(EC.url_contains("/products"))
        self.driver.find_element(*self.search_product).send_keys(product_name)
    
    def select_brand(self):
        brand_locator = (By.XPATH,'/html/body/section[2]/div[1]/div/div[1]/div[1]/div[2]/div/ul/li[1]/a')
        self.driver.find_element(*brand_locator).click()

    