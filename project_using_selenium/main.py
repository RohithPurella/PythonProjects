import time

from secure import pw

from selenium import webdriver


class NaukriBot:
    def __init__(self, pw):
        driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
        driver.get("https://www.naukri.com/mnjuser/profile?id=&orgn=homepage")
        time.sleep(5)
        emailBox = driver.find_element_by_id("usernameField")
        emailBox.send_keys("rohit.purella@gmail.com")  # Enter here your naukri mail address
        password_box = driver.find_element_by_id("passwordField")
        password_box.send_keys(pw)  # Enter here your password of naukri or create new file and import file and us variable here like me :)
        login_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[5]/div/button")
        login_button.submit()
        time.sleep(5)
        privacy = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/button")
        privacy.click()  # For any popup use this to agree T&C of WEBSITE
        upload_box = driver.find_element_by_xpath("/html/body/div[2]/div/div/span/div/div/div/div/div/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div/div[1]/div[1]/section/div/div[1]/input")
        upload_box.send_keys("C:\\Users\\rohit\\Downloads\\Rohith_Resume.docx")  # Provide file address here py using \\ symbols
        time.sleep(10)


NaukriBot(pw)  # provide variables specified in method or functions

# THIS PROJECT IS DONE IN WINDOWS SO THE PATH WILL VARIES FROM DIFFERENT OPERATING SYSTEMS
