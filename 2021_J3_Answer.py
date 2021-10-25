import math

print(" ")
a = int(input("1st Bid:$"))
b = raw_input("Name: ")
print(" ")
c = int(input("2nd Bid: $"))
d = raw_input("Name: ")
print(" ")
e = int(input("3rd Bid: $"))
f = raw_input("Name: ")

if (a >= c >= e):
    print("the highest bidder is placed by " + b)
if (c >= e >= a):
    print("the highest bidder is placed by " + d)
if (e >= a >= c):
    print("the highest bidder is placed by " + f)