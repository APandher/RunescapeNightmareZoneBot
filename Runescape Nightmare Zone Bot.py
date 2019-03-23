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
    pyautogui.click(pyautogui.moveTo(random.randint(a-5,a-2),random.randint(b-5,b-2)), duration = random.uniform(0.5,1))
    time.sleep(random.uniform(1,2))
    pyautogui.click(pyautogui.moveTo(random.randint(a-5,a-2),random.randint(b-5,b-2)), duration = random.uniform(0.5,1))

def overload():
    overloadCoordinates = overloadList[0]
    c,d = pyautogui.center(overloadCoordinates)
    pyautogui.click(pyautogui.moveTo(random.randint(c-2,c),random.randint(d,d+2)),duration = random.uniform(1,1.5))
    overloadList.append(overloadList[0])
    overloadList.remove(overloadList[0])

def absorption():
    absorptionCoordinates = absorptionList[0]
    e,f = pyautogui.center(absorptionCoordinates)
    pyautogui.click(pyautogui.moveTo(random.randint(e-2,e),random.randint(f,f+2)),duration = random.uniform(1,1.5))
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
    pyautogui.click(pyautogui.moveTo(random.randint(g-2,g),random.randint(h,h+2)),duration = random.uniform(1,1.5))
    logout2Cord = pyautogui.locateOnScreen('Nightmare Zone Bot Pictures/logout2.png')
    i,j = pyautogui.center(logout2Cord)
    pyautogui.click(pyautogui.moveTo(random.randint(i-2,i),random.randint(j,j+2)),duration = random.uniform(1,1.5))




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



//Make a class for this, start modularizing the code as it is repetitive 






    





    





        

