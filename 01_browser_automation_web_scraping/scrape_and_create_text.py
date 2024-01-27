from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt
import os
import time


def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")

    return driver


def clean_text(text):
    print(text)
    output = float(text.split(": ")[1])
    return output


def write_file(text):
    """Write input text into a text file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    output_directory = "/Users/johnsims/Desktop/automate_everything_python/01_browser_automation_web_scraping/output"
    os.makedirs(output_directory, exist_ok=True)
    filepath = os.path.join(output_directory, filename)
    with open(filepath, "w") as file:
        file.write(text)


def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    driver.find_element(by="id", value="id_password").send_keys(
        "automatedautomated" + Keys.RETURN
    )
    count = 0
    while count < 4:
        time.sleep(4)
        print("waiting")
        element = driver.find_element(by="xpath", value="/html/body/div[1]/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)
        count += 1
    return "Great job, John."


print(main())
