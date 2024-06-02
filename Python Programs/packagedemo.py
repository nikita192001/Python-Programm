#program file- packagedemo.py
# import user defined package in a program

from mypackage import evenodd as e

#accept
num=int(input("\n\n Enter any number : "))

#check

e.check_even_odd(num)