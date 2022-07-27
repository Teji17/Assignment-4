class Vehicle:
    def __del__(self):
        print("Vehicle object destroyed")
        print(10/0)
v = Vehicle()
del v

#Vehicle object destroyed
#Exception ignored in: <function Vehicle.__del__ at 0x00000146E3D86AF0>
#Traceback (most recent call last):
#File "C:\Users\HP\Desktop\Assignment 4\9.py", line 4, in __del__
#print(10/0)
#ZeroDivisionError: division by zero
