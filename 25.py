
fibonacci_list = [1,1]
even_fibonacci_list = list()
count = 2

while len(str(fibonacci_list[-1])) < 1000 :
    next_fibonacci_element =fibonacci_list[-2]+fibonacci_list[-1]
    fibonacci_list.append(next_fibonacci_element)
    count += 1




print(count)
