#selenium -> controlling browser activities
#webdriver_manager -> to manage the browser drivers automatically


from selenium import webdriver
from selenium.webdriver.common.by import By #to locate elements on the webpage
from selenium.webdriver.common.keys import Keys #to send keyboard inputs
from selenium.webdriver.common.action_chains import ActionChains #to perform complex user interactions like mouse movements, clicks, and keyboard actions
from selenium.webdriver.chrome.service import Service #to manage the ChromeDriver service
from webdriver_manager.chrome import ChromeDriverManager #to manage ChromeDriver automatically
from selenium.webdriver.support.ui import WebDriverWait #to wait for certain conditions to be met before proceeding with the next steps
from selenium.webdriver.support import expected_conditions as EC #to define expected conditions for WebDriverWait, such as waiting for an element to be clickable or visible
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #automatically downloads and sets up the ChromeDriver
driver.get("https://www.linkedin.com/login") 

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password") #locating the username and password fields using their IDs

username.send_keys("rautjay12345@student.sfit.ac.in") #types username automatically into the username field
password.send_keys("********") #types password automatically into the password field

login_button = driver.find_element(By.XPATH, "//button[@type='submit']") #locating the login button using its XPath(used to locate elements based on their position in the HTML structure)
login_button.click() #clicking the login button to submit the form

time.sleep(3) # wait for 3 seconds

search_box = driver.find_element(By.CSS_SELECTOR,".search-global-typeahead__input.search-global-typeahead__input--ellipsis") #locating the search box using its CSS selector
search_box.send_keys("Python Developer")
search_box.send_keys(Keys.RETURN) #pressing the Enter key to submit the search query
time.sleep(5) # wait for 5 seconds

try:
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") #scrolling to the bottom of the page to load more results
        time.sleep(3)

        connect_buttons = driver.find_elements(By.XPATH,"//button[.//span[contains(@class, 'artdeco-button--secondary') and contains(text(), 'Connect')]]") #locating all the "Connect" buttons on the page

        if not connect_buttons:
            print("No 'connect' buttons found")
            break

        for button in connect_buttons:
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", button) #scrolling to the button to ensure it's visible
                time.sleep(1)

                try:
                    button.click()
                except:
                    driver.execute_script("arguments[0].click();", button) #if the normal click doesn't work, use JavaScript to click the button

                time.sleep(2)

                try:
                 send_without_note_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
               (By.XPATH, "//button[.//span[contains(@class, 'artdeco-button__text') and text()='Send without a note']]")
                )
                    )
                 send_without_note_button.click() #clicking the "Send without a note" button to send the connection request
                 print("Connection request sent")
                 time.sleep(2)

                except Exception as send_error:
                    print(f"Error finding 'Send without a note' button: {send_error}")
            except Exception as click_error:
                print(f"Error clicking 'Connect' button: {click_error}")



except KeyboardInterrupt:
    print("Process Interrupted by user!!")

driver.quit() 

