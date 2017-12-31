#Sum square difference
number = 0
sum = 0
total= 0
totalsum = 0
numbersum= 0

for x in range(1,101):
    number = x*x
    total = total + number

for x in range(1,101):
    numbersum = numbersum + x

totalsum = numbersum * numbersum

value= totalsum - total
print(value)







