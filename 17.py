from num2words import num2words

letter_count = list()

for number in range(1,1001):
    words = num2words(number)
    word_list = list(words)
    for letters in word_list :
        if letters == ' ' or letters == '-' or letters == ',':
            word_list.remove(letters)

    letter_count += word_list


print(len(letter_count))


#
#
#
#

#



# for i in m:
#     print(list(i))