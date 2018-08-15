print("lekcja10")  ##operatory logiczne 

fruits=['apple','orange','pear', 'banana', 'apple', 'strawbarry', 'apple', 'berry']

if "orange" in fruits:
    print("znaleziono pomarancze")
else: 
    if "apple" in fruits:
        print(" Znaleziono jabłko ")
    else  :
        print("Nie znaleziono")


if "orange" in fruits :
    print("znaleziono pomarancze")
elif "apple" in fruits:
    print(" Znaleziono jabłko ")
elif True  :
    print("Nie znaleziono")





import time

print("start")
##print(time.time())
##time.sleep(5)

print("stop")

timer=time.time()
time.sleep(2)
timer2=time.time()
elapsed=0
elapsed=timer2 - timer
print(elapsed)


##while True:
 ##   if time.time()-timer>2:
   ##     print("minelo 2 sekundy ")
     ##   timer=time.time()

  ##  if time.time()-timer2>1:
    ##    print("minelo 1 sekundy ")
      ##  timer2=time.time()

import datetime

teraz = datetime.datetime.now()

print(str(teraz.hour) +":" +str(teraz.minute))

print(teraz.strftime("%M"))