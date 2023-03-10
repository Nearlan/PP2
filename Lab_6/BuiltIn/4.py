from time import sleep
from math import sqrt
n = int(input())
time = int(input())
sleep(time / 1000)
print("Square root of", n, "after", time, "miliseconds is", sqrt(n))
