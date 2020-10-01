from selenium import webdriver
import time

#creates driver, opens cookie clicker, and waits so the site can load
driver = webdriver.Firefox(executable_path=r'C:\Program Files\geckodriver.exe')
driver.get('https://orteil.dashnet.org/cookieclicker/')
time.sleep(2)

#creates an object for the cookie and all the products
cookie = driver.find_element_by_xpath('//*[@id="bigCookie"]')
p0 = driver.find_element_by_xpath('//*[@id="product0"]')
p1 = driver.find_element_by_xpath('//*[@id="product1"]')
p2 = driver.find_element_by_xpath('//*[@id="product2"]')
p3 = driver.find_element_by_xpath('//*[@id="product3"]')
p4 = driver.find_element_by_xpath('//*[@id="product4"]')
p5 = driver.find_element_by_xpath('//*[@id="product5"]')
p6 = driver.find_element_by_xpath('//*[@id="product6"]')
p7 = driver.find_element_by_xpath('//*[@id="product7"]')
p8 = driver.find_element_by_xpath('//*[@id="product8"]')
p9 = driver.find_element_by_xpath('//*[@id="product9"]')
p10 = driver.find_element_by_xpath('//*[@id="product10"]')
p11 = driver.find_element_by_xpath('//*[@id="product11"]')
p12 = driver.find_element_by_xpath('//*[@id="product12"]')
p13 = driver.find_element_by_xpath('//*[@id="product13"]')
p14 = driver.find_element_by_xpath('//*[@id="product14"]')
p15 = driver.find_element_by_xpath('//*[@id="product15"]')
p16 = driver.find_element_by_xpath('//*[@id="product16"]')

#removes cookies banner
driver.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()

#infinite loop that clicks the cookie and then buys any available product, prioritizing upgrades and then the most valuable product
while True:
    cookie.click()
    if len(driver.find_elements_by_id("upgrade0")) > 0 and driver.find_element_by_id("upgrade0").get_attribute('class') == "crate upgrade enabled":
        driver.find_element_by_id("upgrade0").click()
    elif p16.get_attribute('class') == "product unlocked enabled":
        p16.click()
    elif p15.get_attribute('class') == "product unlocked enabled":
        p15.click()
    elif p14.get_attribute('class') == "product unlocked enabled":
        p14.click()
    elif p13.get_attribute('class') == "product unlocked enabled":
        p13.click()
    elif p12.get_attribute('class') == "product unlocked enabled":
        p12.click()
    elif p11.get_attribute('class') == "product unlocked enabled":
        p11.click()
    elif p10.get_attribute('class') == "product unlocked enabled":
        p10.click()
    elif p9.get_attribute('class') == "product unlocked enabled":
        p9.click()
    elif p8.get_attribute('class') == "product unlocked enabled":
        p8.click()
    elif p7.get_attribute('class') == "product unlocked enabled":
        p7.click()
    elif p6.get_attribute('class') == "product unlocked enabled":
        p6.click()
    elif p5.get_attribute('class') == "product unlocked enabled":
        p5.click()
    elif p4.get_attribute('class') == "product unlocked enabled":
        p4.click()
    elif p3.get_attribute('class') == "product unlocked enabled":
        p3.click()
    elif p2.get_attribute('class') == "product unlocked enabled":
        p2.click()
    elif p1.get_attribute('class') == "product unlocked enabled":
        p1.click()
    elif p0.get_attribute('class') == "product unlocked enabled":
        p0.click()
