from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.netflix.com/vn/")

# driver.implicitly_wait(0.5)


# login account
login_button = driver.find_element(by=By.ID, value="signIn")
login_button.click()
time.sleep(2)


email_input = driver.find_element(By.NAME, "userLoginId")
email_input.send_keys("khoa662003@gmail.com")
time.sleep(2)
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys("Khoavo662003")
time.sleep(2)


login = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/form/button[1]")
login.click()
time.sleep(2)


button_user = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div")
button_user.click()
time.sleep(2)


# search film
search_box = driver.find_element(By.CLASS_NAME, "searchTab")
search_box.click()
search_input = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div/input")
search_input.send_keys("Conan")
search_input.send_keys(Keys.ENTER)

time.sleep(2)


#logout
menu_account = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div[4]/div/div")

account_icon = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-dropdown-button"))
)
ActionChains(driver).move_to_element(account_icon).perform()
        
        # Nhấp vào nút đăng xuất
logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sign out of Netflix')]"))
)
logout_button.click()
        
#         # Xác minh rằng đã đăng xuất thành công
# WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
# )
# print("Đăng xuất thành công!")
    
time.sleep(10)

driver.quit()
