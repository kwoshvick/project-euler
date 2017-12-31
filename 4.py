
palindrome_list = list()

def is_palindrom(number):

    number = str(number)
    reversed_number = reverse_it(number)
    if number == reversed_number:
        if number not in palindrome_list:
            palindrome_list.append(int(number))



def reverse_it(number):
    reversed_number = number[::-1]
    return reversed_number

for first_number in range(100,1000):
    for second_number in range(100,1000):
        multiplication = first_number * second_number
        is_palindrom(multiplication)

print(max(palindrome_list))


