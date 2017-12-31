
#Multiples of 3 and 5

limit = 1000
multiple_array = list()
counter  = 1

while counter < 1000:
    if counter % 3 == 0 or counter % 5 ==0:
        multiple_array.append(counter)
        counter+=1
    else:
        counter+=1

sum_of_multiples = sum(multiple_array)

print("The ssum is " , sum_of_multiples)







