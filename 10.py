prime = list()


def isPrime(start):
    number = start
    counter = 2
    if(counter == start):
        prime.append(number)

    while (counter < number):


        if ((number % counter) == 0):
            break

        if ((counter + 1) == number ):
            prime.append(number)

        counter += 1


start = 1
end = 10
while(start < end):
    isPrime(start)
    start += 1
    #print(start)

print(sum(prime))



# print(divisors)