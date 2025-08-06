import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import random

def send_keys_slowly(element, text, min_delay=0.0, max_delay=0.0):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

def main():
    driver = uc.Chrome(version_main=138)

    with open("users.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            username = row["username".strip()]
            password = row["password".strip()]
            email = row["email".strip()]

            driver.get("https://vjudge.net/")

            register_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_button.click()

            WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.ID, "register-username"))
            )

            username_field = driver.find_element(By.ID, "register-username")
            username_field.clear()
            send_keys_slowly(username_field, username)

            password_field = driver.find_element(By.ID, "register-password")
            password_field.clear()
            send_keys_slowly(password_field, password)

            repeat_password_field = driver.find_element(By.ID, "register-repeat-password")
            repeat_password_field.clear()
            send_keys_slowly(repeat_password_field, password)

            email_field = driver.find_element(By.ID, "register-email")
            email_field.clear()
            send_keys_slowly(email_field, email)

            print(f"\n🛑 Please solve the CAPTCHA and click 'Register' for user: {username}")
            input("✅ After completing registration, press ENTER to continue to next user...")

    print("🎉 All users processed. You can close the browser now.")

if __name__ == "__main__":
    main()

