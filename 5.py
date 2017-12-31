#lazy method

counter  = 21

while True:
    if counter % 3 == 0 and counter % 4 ==0 and counter % 5 ==0 and counter % 6 ==0 \
            and counter % 7 == 0 and counter % 8 ==0 and counter % 9 ==0 and counter % 10 ==0 \
            and counter % 11 == 0 and counter % 12 ==0 and counter % 13 ==0 and counter % 14 ==0 \
            and counter % 15 == 0 and counter % 16 ==0 and counter % 17 ==0 and counter % 18 ==0 \
            and counter % 19 == 0 and counter % 20 ==0:
        print(counter)
        break
    else:
        counter+=1