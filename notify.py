import time
from plyer import notification

while(True):
    notification.notify(
        title="Start Coding Now!", 
        message="You need to rise and start doing what you love doing - coding.",
        app_icon="Allo.png",
        timeout=5)
    time.sleep(10)