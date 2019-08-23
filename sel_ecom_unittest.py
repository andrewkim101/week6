from selenium import webdriver
import time
import unittest

class SeleniumTest(unittest.TestCase):

    # test data
    __website_path = "http://automationpractice.com/index.php"

    @classmethod
    def setUpClass(cls):
        """initialize the browser and opens the page"""
        # paste the chromedriver in this location : C:\Program Files\Python37 (python installation folder)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # open the page and enter the keyword
        cls.driver.get(cls.__website_path)


    def test_verify_product_names(self):
        """get the product name of listed products, search should be done before this function"""
        word = 'dress'

        self.search_keyword(word)

        product_name_list = self.driver.find_elements_by_xpath("//div[@id='center_column']//a[@class='product-name']")
        for element in product_name_list:
            self.assertTrue(word.lower() in element.text.lower())
            # if word.lower() in element.text.lower():
            #     print(f"Test passed for {element.text}")
            # else:
            #     print(f"Test FAILED for {element.text}")
    
    def test_verify_signin_button(self):
        # check sign in button 
        signin_button = self.driver.find_element_by_link_text("Sign in")
        self.assertTrue(signin_button.is_enabled)
        # if signin_button.is_displayed:
        #     print("sign in button test passed")
        # else:
        #     print("sign in button FAILED")

    def test_verify_cart_status(self):
        css_selector = 'span.ajax_cart_no_product'
        cart_status = self.driver.find_element_by_css_selector(css_selector)
        self.assertTrue(cart_status.is_displayed)
        # if cart_status.is_displayed:
        #     print(f"Cart status Passed , text: {cart_status.text}")
        # else: 
        #     print("cart status FAILED")

    @classmethod
    def tearDownClass(cls):
        # close the browser
        cls.driver.quit()


    def verify_menu_items(self):
        top_menu_list = self.driver.find_elements_by_tag_name("li")
        print(len(top_menu_list))

    def minimize_browser(self):
        self.driver.minimize_window()

    def search_keyword(self, word):
        search_field = self.driver.find_element_by_name('search_query')
        time.sleep(5)
        search_field.send_keys(word)
        time.sleep(5)
        search_field.submit()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main(verbosity=2)