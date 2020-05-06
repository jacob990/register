import time
import random
print("#################################################################")
time.sleep(1.5)
print("Welcome to our login page")
time.sleep(1)
a = str(input("Enter your name:"))
time.sleep(0.5)
print("Welcome",a,"!!!")
b = str(input("Enter your username :"))
time.sleep(1)
c = str(input("Enter your password  :"))
time.sleep(1)
d = str(input("Retype your password  :"))
time.sleep(1)
if(c==d):
    print("Password Matched!!")
else:
    print("Please enter correctly!!")
    e = input("")
    if(e == c):
        print("Password Matched!!")
    else:
        print("Please enter Correctly!!")
        f = input("")
        if(f == c):
            print("Password matched!!")
        else:
            print("Please enter Correctly!!")
e = str(input("Enter your email:"))
time.sleep(1)
print("You had been Login successfully !!!")
