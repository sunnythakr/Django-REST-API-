from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# chrome driver - chrome browser  
service_obj = Service() # seleniummanager
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.youtube.com/")



# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")