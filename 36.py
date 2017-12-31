
m = bin(585).zfill(8)
m = m.lstrip('-0b')



palindrome_list = list()

def is_palindrom(number):

    number = str(number)
    reversed_number = reverse_it(number)
    if number == reversed_number:
        binary_number = bin(int(number))
        binary_number = binary_number.lstrip('-0b')
        binary_number = str(binary_number)
        reversed_binary = reverse_it(binary_number)
        if reversed_binary == binary_number:
            if number not in palindrome_list:
                palindrome_list.append(int(number))




def reverse_it(number):
    reversed_number = number[::-1]
    return reversed_number

for first_number in range(1,1000000):
    is_palindrom(first_number)

print(sum(palindrome_list))
