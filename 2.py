
#Even Fibonacci numbers

fibonacci_list = [0,1]
even_fibonacci_list = list()

while fibonacci_list[-1] < 4000000:
    next_fibonacci_element =fibonacci_list[-2]+fibonacci_list[-1]
    fibonacci_list.append(next_fibonacci_element)


for number in fibonacci_list:
    if number % 2 == 0:
        even_fibonacci_list.append(number)


sum_of_even_fibonacci = sum(even_fibonacci_list)

print(sum_of_even_fibonacci)


