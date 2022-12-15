from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

controlador = webdriver.Chrome(executable_path= "C:\Program Files\driver\chromedriver.exe")
controlador.get ("https://lavandanatural.com")
controlador.maximize_window()
time.sleep(3)

productos = controlador.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/header[1]/div[1]/ul[1]/li[2]/a[1]")
productos.click()
time.sleep(3)


requirement = ()  #Expected Result
labelObtained = ()  #Actual Result

def compareLabels():
    if requirement in labelObtained:
        print ("Pass")
    else:
        print ("Fail")


campoProductos = controlador.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/header[1]/div[1]/ul[1]/li[2]/a[1]")

labelCampoProductos = controlador.find_element(By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[4]/div[1]/header[1]/div[1]/ul[1]/li[2]/a[1]").text

labelObtained =labelCampoProductos
print(labelObtained)

requirement = 'PRODUCTOS'

compareLabels()

controlador.close()