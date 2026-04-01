from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class login_page():

    def __init__(self, context):
        self.driver = context.driver

    def open_url(self):
        self.driver.get("https://www.amazon.in/")

    def validate_page(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@data-id='c4b28d0']")))

    def enter_name(self, name):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='firstname']"))).send_keys(name)

    def enter_email(self, email):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys(email)

    def enter_company(self, comp_name):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='field[44]']"))).send_keys(comp_name)

    def enter_job(self, job_name):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='field[43]']"))).send_keys(job_name)

    def select_country(self, country):
        dropdown = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='iti__arrow']")))
        dropdown.click()
        search_country = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@class='iti__search-input']")))
        search_country.send_keys(country)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//span[text()='India']"))).click()

    def enter_phn_number(self, phn_num):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))).send_keys(phn_num)


    def select_service(self):
        dropdown = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//select[@id='field[168]']")))
        select = Select(dropdown)
        select.select_by_visible_text("EDI Services")


    def click_btn(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@id='_form_375_submit']"))).click()