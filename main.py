import time 
from plyer import notification 

if __name__ == "__main__":
    notification.notify(
        app_name = "Drinkify by THE TECHNOSTIC",
        title = "Please Drink Water",
        message = "TYPE YOUR OWN MESSAGE HERE!",
        timeout = 12
        
        
    )
    time.sleep(60*60)
