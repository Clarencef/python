import webbrowser
import time

count = 0
while (count < 3):
    time.sleep(2)
    webbrowser.open('http://www.youtube.com')
    count += 1
