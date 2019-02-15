from selenium import webdriver
from getpass import getpass
import requests

usr='xxx'
pwd='xxx'

driver=webdriver.Chrome('C:\\Users\\bellapukonda\\Desktop\\auto\\chromedriver.exe')
driver.get('http://placement.bitmesra.ac.in/')
username_box=driver.find_element_by_id('txtUsername')
username_box.send_keys(usr)
pass_box=driver.find_element_by_id('txtPassword')
pass_box.send_keys(pwd)
login_box=driver.find_element_by_id('imgSubmit')
login_box.click()


driver.get("http://placement.bitmesra.ac.in/Student/Jobs.aspx")
d={}
url=driver.find_element_by_id("cname1").get_attribute("href")
urls=driver.find_elements_by_id("cname1")
b=[]
for i in urls:
    b.append(i.get_attribute("href"))
anc= driver.find_element_by_xpath("//a[text()='2']")
anc.click()
url=driver.find_element_by_id("cname1").get_attribute("href")
urls=driver.find_elements_by_id("cname1")

for i in urls:
    b.append(i.get_attribute("href"))
anc= driver.find_element_by_xpath("//a[text()='3']")
anc.click()
url=driver.find_element_by_id("cname1").get_attribute("href")
urls=driver.find_elements_by_id("cname1")
for i in urls:
    b.append(i.get_attribute("href"))
anc= driver.find_element_by_xpath("//a[text()='4']")
anc.click()
url=driver.find_element_by_id("cname1").get_attribute("href")
urls=driver.find_elements_by_id("cname1")
for i in urls:
    b.append(i.get_attribute("href"))





for i in b:
    driver.get(i)    
    a=driver.find_elements_by_class_name('col-xs-3 ')
    for i in a:
        s=i.text
        if('-' in s):
            s=s.split('-')
            if(s[0] in d):
                d[s[0]].append(s[1])
            else:
                d[s[0]]=[s[1]]


driver.quit()





    

