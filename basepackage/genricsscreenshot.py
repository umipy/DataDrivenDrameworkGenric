import time
def getScreenShot(driver):
    path='F:\\DataDrivenDrameworkGenric\\screenshots\\'
    #path='D:\\demoproject\\screenshots\\'
    name=str(round(time.time()))+'.png'
    value=path+name
    driver.save_screenshot(value)