prime_factors = list()
prime_numbers = list()
prime_number = list()

import sys

number = 600851475143



for first_number in range(2,number):

    count = 0
    stop = first_number
    for second_number in range(2, stop):
        if int(first_number) % int(second_number) == 0  :
            count += 1

    if count == 0:
        if number % first_number == 0:
            prime_factors.append(first_number)



#    if len(prime_number) == 10001: break

print(max(prime_factors))