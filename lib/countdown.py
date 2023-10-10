# your code goes here!
#import time for sleep function


import time
def countdown(number):
    while number >0:
        print(f'{number} SECOND(S)!')
        number -=1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        #makes the loop pause for one second each iteration
        time.sleep(1) 
        number -= 1
    print('HAPPY NEW YEAR!')

countdown(5)
countdown_with_sleep(5)

