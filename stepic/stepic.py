fileNameRead = 'Denis.txt'
fileNameWrite = 'Denis1.txt'
file = open(fileNameRead,'r')
string = file.readline().strip()
file.close()
newstring1 = ''
y = ''
z = ''
i = 0
number = ''
xi = 0
file = open(fileNameWrite, 'w')
while i < len(string):
    y = string[i]
    if (y.isalpha()) == True:
        newstring1 = ''
        newstring1 += y
    else:
        number = ''
        xi = i
        if i != (len(string)-1):
            while y.isdigit() == True:
                number += y
                if (xi + 1) < len(string):
                    xi += 1


            y = string[xi]
            number = int(number)
            file.write(newstring1 * number)
        if i == (len(string)-1):
            number += y
            number = int(number)
            file.write(newstring1 * number)
    if i < xi:
        i = xi
    else:
        i += 1
file.close()
