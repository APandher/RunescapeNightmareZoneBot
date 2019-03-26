import time
import pyautogui
import random
import sys
import schedule

counter = 0
overloadList  = list(pyautogui.locateAllOnScreen('Nightmare Zone Bot Pictures/Overload Potion.png'))
print(overloadList)
absorptionList = list(pyautogui.locateAllOnScreen('Nightmare Zone Bot Pictures/Absorption Potion.png'))

def hpReset():
    startTime1 = time.time()
    prayCord = pyautogui.locateOnScreen('Nightmare Zone Bot Pictures/Prayer Protect.png')
    a,b = pyautogui.center(prayCord)
    click(a,b)
    time.sleep(random.uniform(1,2))
    click(a,b)

def overload():
    overloadCoordinates = overloadList[0]
    c,d = pyautogui.center(overloadCoordinates)
    click(c,d)
    overloadList.append(overloadList[0])
    overloadList.remove(overloadList[0])

def absorption():
    absorptionCoordinates = absorptionList[0]
    e,f = pyautogui.center(absorptionCoordinates)
    click(e,f)
    absorptionList.append(absorptionList[0])
    absorptionList.remove(absorptionList[0])

def initialization():
    global counter

    if counter == 1:
        pass

    else:
        overload 
        counter += 1

def logout():
    logout1Cord = pyautogui.locateOnScreen('Nightmare Zone Bot Pictures/logout1.png')
    g,h = pyautogui.center(logout1Cord)
    click(g,h)
    logout2Cord = pyautogui.locateOnScreen('Nightmare Zone Bot Pictures/logout2.png')
    i,j = pyautogui.center(logout2Cord)
    click(i,j)



def main():

    overload()
    schedule.every(random.uniform(302,304)).seconds.do(overload)
    schedule.every(random.uniform(40,45)).seconds.do(hpReset)
    schedule.every(random.uniform(180,183)).seconds.do(absorption)

    while 1:
        schedule.run_pending()
        time.sleep(1)

    if pyautogui.locateOnScreen('Nightmare Zone Bot Pictures/logout.png') == True:
        logout()
        
 def click(e,f):
    pyautogui.click(pyautogui.moveTo(random.randint(e-2,e),random.randint(f,f+2)),duration = random.uniform(1,1.5))



//Make a class for this, start modularizing the code as it is repetitive 






    





    





        

