from threading import Thread
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '93.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '100.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': '10',
      'os': 'Windows',
      'browser': 'ie',
      'browser_version': '11.0',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
     },
     {
      'os_version': '11',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '99.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'os_version': '11',
      'os': 'Windows',
      'browser': 'edge',
      'browser_version': '100.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      }]
#run_session function searches for 'BrowserStack' on BrowserStack
def run_session(desired_cap):
    driver = webdriver.Remote(
      command_executor='https://alikh_9FlHdU:vrPJFXzs2dSGfYkZyzFa@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.browserstack.com/")
    WebDriverWait(driver, 10).until(EC.title_contains("BrowserStack"))
    #Get the title of the homepage and verify it
    # Maximize the window
    driver.maximize_window()


    try:
        # Get the Text on the top og the homepage and verify its as expected
        title_on_homepage = wait.until(EC.visibility_of_element_located((By.XPATH, '//main[@id="main-content"]//h1'))).text
        if title_on_homepage == "App & Browser Testing Made Easy":
            # Set the status of test as 'passed' or 'failed' based on the condition;if the title that expected to be 'App & Browser Testing Made Easy'
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title of the home page is as expected"}}')   
            
    except NoSuchElementException:
        driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title of the homepage is NOT as expected"}}')
    
    try:    
        # Click on Live link
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='relative']//a[@title='Live']"))).click()
        # Get the title text on the top og the Live page and verify its as expected
        title_on_live_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='sec-header-title']//span"))).text
        if title_on_live_page == "Live":
            # Set the status of test as 'passed' or 'failed' based on the condition;if the title that expected to be 'App & Browser Testing Made Easy'
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title of the Live page is as expected"}}')
    except NoSuchElementException:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title of Live page is NOT as Expected"}}')

    # get back to the homepage
    driver.back()

        # Click on Automate link
    try:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='relative']//a[@title='Automate']"))).click()
        # Get the title text on the top og the Automate page and verify its as expected
        title_on_live_page = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@id='sec-header-title']//span"))).text
        if title_on_live_page == "Automate":
            # Set the status of test as 'passed' or 'failed' based on the condition;if the title that expected to be 'App & Browser Testing Made Easy'
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title of the Automate page is as expected"}}')
    except NoSuchElementException:
            driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title of Automate page is NOT as Expected"}}')

    # Stop the driver
    driver.quit()
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()