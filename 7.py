import sys
prime_number = list()



for first_number in range(2,sys.maxsize):
    #print('firs',first_number)
    count = 0
    stop = first_number
    for second_number in range(2, stop):
        #print((first_number) / int(second_number ),' ' , first_number, ' ', second_number )
        if int(first_number) % int(second_number) == 0  :
            count += 1
            #if count > 2 : break
    #print('count',count)
    if count == 0:
        prime_number.append(first_number)
    if len(prime_number) == 10001: break

print(prime_number[-1])

