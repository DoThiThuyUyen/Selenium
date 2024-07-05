from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.netflix.com/vn/")

# fc login to Netflix
def login_netflix(email, password):
    try:
        # Click on the sign in button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "signIn"))
        )
        login_button.click()

        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "userLoginId"))
        )
        email_input.send_keys(email)

        # Enter password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)

        # Click on the login button
        
        login = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/form/button[1]")
        login.click()
        time.sleep(2)

        #select profile icon
        button_user = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div")
        button_user.click()
        time.sleep(2)
        print("Login sucess")
        
    except Exception as e:
        print("Login failed: ", e)

# search film
def search_film(film_name):
    try:
        # Click on the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "searchTab"))
        )
        search_box.click()

        # Enter the film name in the search input
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Titles, people, genres']"))
        )
        search_input.send_keys(film_name)
        search_input.send_keys(Keys.ENTER)

        # See the results
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "title-card-container"))
        )
        print(f"Search results for '{film_name}' are displayed.")
    except Exception as e:
        print("Search failed:", e)

#fc logout to netflix
def logout_netflix(driver):
    try:

        account_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-dropdown-button"))
        )
        ActionChains(driver).move_to_element(account_icon).perform()
        

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign out of Netflix')]"))
        )
        logout_button.click()
        

        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
        # )
        time.sleep(2)
        print("Logout sucess")
        
    except Exception as e:
        print("Logout failed:", e)


email = "khoa662003@gmail.com"
password = "Khoavo662003"
film_name = "Conan"

login_netflix(email, password)
search_film(film_name)
logout_netflix(driver)
time.sleep(10)
driver.quit()
