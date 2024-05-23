# Numbers.txt challenge
import random

numbersList = ["a", "b", "c", "d", "e"]
nls = numbersList
numbersList[:] = [random.randrange(10) for x in numbersList]

for x in nls:
    print(x)

print("The total is: ")
print(sum(nls))
