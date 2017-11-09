import webbrowser
import time

i=0
while i < 3:
    person = input('Do you want a break?')
    if (person == 'yes') :
        time.sleep(5)
        webbrowser.open("www.yahoo.com")
    else:
        print("User doesnt want break:")
    i = i + 1    
   
