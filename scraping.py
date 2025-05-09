from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")

time.sleep(3)  
search_box = driver.find_element(By.ID, "searchboxinput")
search_box.send_keys("company near me")
search_box.send_keys(Keys.ENTER)

time.sleep(5)
companies = set()
scroll_count = 0

while len(companies) < 30 and scroll_count < 10:
    cards = driver.find_elements(By.XPATH,'//div[contains(@class, "Nv2PK")]')

    for card in cards:
        try:
            name = card.find_element(By.CLASS_NAME, "qBF1Pd").text
            driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(1)
            driver.execute_script("arguments[0].click();", card)
            time.sleep(3)

            try:
                website = driver.find_element(By.XPATH, '//a[contains(@class,"CsEnBe") and contains(@aria-label, "Website")]').get_attribute('href')
            except:
                website = "N/A"
           
            try:
                phone = driver.find_element(By.XPATH, '//button[contains(@class,"CsEnBe") and contains(@aria-label = "Phone")]').get_attribute('aria-label').split()[-1].strip()
            except Exception as e:
                print("phone error:", e)               
                phone = "N/A"        
            
            companies.add((name,phone,website))
        except:
            continue

    scrollable = driver.find_element(By.XPATH,'//div[@role="feed"]')
    driver.execute_script("arguments[0].scrollBy(0, 1000);",scrollable)
    time.sleep(2)
    scroll_count += 1

i = 1
for company in companies:
    name, phone, website = company
    print(str(i)+ "."+ name +"|" +phone +"|"+ website)
    i += 1

driver.quit()

df = pd.DataFrame(list(companies), columns=["Name", "Phone", "Website"])


df.to_excel("companies2.xlsx", index=False)