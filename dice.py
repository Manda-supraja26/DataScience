import random as rd
import time
t0=time.time()
def call():
    x=int(input("enter the your dice value: "))
    y=rd.choice([1,2,3,4,5,6])
    print("the value from computer", y)
    if x == y:
        call()
    elif x > y:
        print("you won the game")
    else:
        print("you lost the game")
# t1=time.time()
print(t1-t0)
call()
#
# x=int(input("enter the your dice value: "))
# y=rd.choice([1])
# print("the value from computer",y)
# if x==y:
#     call()
# if x>y:
#     print("you won the game")
# else:
#     print("you lost the game")
#