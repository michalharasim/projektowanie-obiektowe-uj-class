import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReactFrontendAuthTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.register_url = "http://localhost:3000/register"
        cls.login_url = "http://localhost:3000/login"
        cls.protected_url = "http://localhost:3000/protected"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_load_home_page(self):
        self.driver.get(self.register_url)
        self.assertIn("React App", self.driver.title)

    def test_02_navigate_to_login_page(self):
        self.driver.get(self.register_url)
        login_link = self.driver.find_element(By.CLASS_NAME, "css-8mezga")
        time.sleep(0.5)
        login_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/login"))
        self.assertIn("/login", self.driver.current_url)



    def test_03_navigate_to_register_page(self):
        self.driver.get(self.login_url)
        register_link = self.driver.find_element(By.CLASS_NAME, "css-8mezga")
        time.sleep(0.5)
        register_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/register"))
        self.assertIn("/register", self.driver.current_url)

    def test_04_navigate_to_protected_page(self):
        self.driver.get(self.login_url)
        register_link = self.driver.find_element(By.CLASS_NAME, "css-4tsmos")
        time.sleep(0.5)
        register_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/protected"))
        self.assertIn("/protected", self.driver.current_url)

    def test_05_navigate_to_login_page_from_protected(self):
        self.driver.get(self.protected_url)
        register_link = self.driver.find_element(By.CLASS_NAME, "css-12gwgo8")
        time.sleep(0.5)
        register_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/login"))
        self.assertIn("/login", self.driver.current_url)

    def test_06_access_protected_page_without_login(self):
        self.driver.get(self.protected_url)
        error_msg = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'css-0'))
        )
        time.sleep(0.5)
        self.assertEqual("You are not authenticated.", error_msg.text)

    def test_07_register_empty_form_validation(self):
        self.driver.get(self.register_url)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_08_register_no_username_validation(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_09_register_no_password_validation(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_10_register_success(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        field_input[1].send_keys('password')
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()

        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Registration successful! Please log in.")
        time.sleep(0.5)
        alert.accept()

    def test_11_register_success_redirects_to_login(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username1')
        field_input[1].send_keys('password1')
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Registration successful! Please log in.")
        time.sleep(0.5)
        alert.accept()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/login"))
        self.assertIn("/login", self.driver.current_url)


    def test_12_login_empty_form_validation(self):
        self.driver.get(self.login_url)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_13_login_no_username_validation(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_14_login_no_password_validation(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()


    def test_15_login_invalid_credentials(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('invalidusername')
        field_input[1].send_keys('invalidpassword')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_16_login_success(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        time.sleep(0.5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Login successful!")
        alert.accept()

    def test_17_login_success_redirects_to_protected(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        time.sleep(0.5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Login successful!")
        alert.accept()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/protected"))
        time.sleep(0.5)
        self.assertIn("/protected", self.driver.current_url)

    def test_18_login_success_gives_access_to_protected(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        time.sleep(0.5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Login successful!")
        alert.accept()
        time.sleep(0.5)
        auth_msg = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'css-0'))
        )
        time.sleep(0.5)
        self.assertEqual("Access granted!", auth_msg.text)


    def test_19_login_fields_typing_and_clearing(self):
        self.driver.get(self.login_url)
        username_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[0]
        password_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[1]
        username_input.send_keys("tempuser")
        password_input.send_keys("temppwd")
        self.assertEqual(username_input.get_attribute("value"), "tempuser")
        self.assertEqual(password_input.get_attribute("value"), "temppwd")
        username_input.clear()
        password_input.clear()
        self.assertEqual(username_input.get_attribute("value"), "")
        self.assertEqual(password_input.get_attribute("value"), "")

    def test_20_register_fields_typing_and_clearing(self):
        self.driver.get(self.register_url)
        username_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[0]
        password_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[1]
        username_input.send_keys("tempuser")
        password_input.send_keys("temppwd")
        self.assertEqual(username_input.get_attribute("value"), "tempuser")
        self.assertEqual(password_input.get_attribute("value"), "temppwd")
        username_input.clear()
        password_input.clear()
        self.assertEqual(username_input.get_attribute("value"), "")
        self.assertEqual(password_input.get_attribute("value"), "")


    def test_21_username_persist_after_failed_login(self):
        self.driver.get(self.login_url)
        username_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[0]
        username_input.send_keys("tempuser")
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        time.sleep(0.5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        time.sleep(0.5)
        self.assertEqual(username_input.get_attribute("value"), "tempuser")

    def test_22_register_fails_if_username_exists(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username1')
        field_input[1].send_keys('password1')
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "An error occurred. Please try again.")
        time.sleep(0.5)
        alert.accept()

    def test_23_register_succeeds_if_password_the_same(self):
        self.driver.get(self.register_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username2')
        field_input[1].send_keys('password1')
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        time.sleep(0.5)
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Registration successful! Please log in.")
        time.sleep(0.5)
        alert.accept()

    def test_24_password_persist_after_failed_login(self):
        self.driver.get(self.login_url)
        password_input = self.driver.find_elements(By.CSS_SELECTOR, "input")[1]
        password_input.send_keys("temppwd")
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        time.sleep(0.5)
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        time.sleep(0.5)
        self.assertEqual(password_input.get_attribute("value"), "temppwd")

    def test_25_after_login_session_is_preserved_for_protected_page(self):
        self.driver.get(self.login_url)
        field_input = self.driver.find_elements(By.CSS_SELECTOR, "input")
        field_input[0].send_keys('username')
        field_input[1].send_keys('password')
        time.sleep(0.5)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')
        submit_btn.click()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        self.assertEqual(alert.text, "Login successful!")
        alert.accept()
        time.sleep(0.5)
        auth_msg = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'css-0'))
        )
        time.sleep(0.5)
        self.assertEqual("Access granted!", auth_msg.text)

        register_link = self.driver.find_element(By.CLASS_NAME, "css-12gwgo8")
        time.sleep(0.5)
        register_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/login"))
        self.assertIn("/login", self.driver.current_url)

        register_link = self.driver.find_element(By.CLASS_NAME, "css-4tsmos")
        time.sleep(0.5)
        register_link.click()
        time.sleep(0.5)
        WebDriverWait(self.driver, 5).until(EC.url_contains("/protected"))
        self.assertIn("/protected", self.driver.current_url)

        auth_msg = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'css-0'))
        )
        time.sleep(0.5)
        self.assertEqual("Access granted!", auth_msg.text)

    def test_26_no_protected_page_button_on_register(self):
        self.driver.get(self.register_url)
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        protected_buttons = [btn for btn in buttons if "protected" in btn.text.lower()]
        self.assertEqual(len(protected_buttons), 0, "Protected page button found on register page!")

    def test_27_register_page_has_username_and_password_inputs(self):
        self.driver.get(self.register_url)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        self.assertEqual(len(inputs), 2, "Register page does not have exactly 2 input fields.")
        self.assertEqual(inputs[0].get_attribute("placeholder").lower(), "username")
        self.assertEqual(inputs[1].get_attribute("placeholder").lower(), "password")

    def test_28_login_page_has_username_and_password_inputs(self):
        self.driver.get(self.login_url)
        inputs = self.driver.find_elements(By.CSS_SELECTOR, "input")
        self.assertEqual(len(inputs), 2, "Register page does not have exactly 2 input fields.")
        self.assertEqual(inputs[0].get_attribute("placeholder").lower(), "username")
        self.assertEqual(inputs[1].get_attribute("placeholder").lower(), "password")

    def test_29_register_button_hover_changes_background_color(self):
        self.driver.get(self.register_url)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')

        before_hover = submit_btn.value_of_css_property('background-color')

        hover = ActionChains(self.driver).move_to_element(submit_btn)
        hover.perform()
        time.sleep(0.5)
        after_hover = submit_btn.value_of_css_property('background-color')
        self.assertNotEqual(before_hover, after_hover, "Background color did not change on hover")


    def test_30_login_button_hover_changes_background_color(self):
        self.driver.get(self.login_url)
        submit_btn = self.driver.find_element(By.CLASS_NAME, 'css-f2zwvg')

        before_hover = submit_btn.value_of_css_property('background-color')

        hover = ActionChains(self.driver).move_to_element(submit_btn)
        hover.perform()
        time.sleep(0.5)
        after_hover = submit_btn.value_of_css_property('background-color')
        self.assertNotEqual(before_hover, after_hover, "Background color did not change on hover")

if __name__ == "__main__":
    unittest.main()
