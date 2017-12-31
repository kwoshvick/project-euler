file = open("13")

sum = 0
for numbers in file:
    #print(numbers.rstrip())

    numbers = int(numbers)
    sum += numbers;


print(sum)

sum = str(sum)

print(sum[:10])
