def is_valid_walk(walk):
    count_n = 0
    count_s = 0
    count_w = 0
    count_e = 0    
    for element in walk:
        if element == 'n':
            count_n += 1
        if element == 's':
            count_s += 1
        if element == 'w':
            count_w += 1
        if element == 'e':
            count_e += 1
    if count_n == count_s and count_w == count_e and ((count_n + count_s + count_w + count_e) == 10):
        print('true')
        return ('true')
    else:
        print('false')
        return ('false')

is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e'])
#Хуй
