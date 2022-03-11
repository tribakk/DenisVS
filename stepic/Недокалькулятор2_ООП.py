def createString(lenght, string):
        spaceSize = lenght - len(string)
        newStr = " " * spaceSize + string
        return newStr

class calcClass(object):
    originalProblem = ""
    firstValue = ""
    secondValue = ""
    operator = ""
    result = 0

    firstStringStr = ""
    secondStringStr = ""
    resultStr = ""
    minusStr = ""

    lenghtCol = 0

    def parseString(self, str):
        originalProblem = str
        str_list = str.split()
        self.firstValue = str_list[0]
        self.operator = str_list[1]
        self.secondValue = str_list[2]

    def calc(self):
        if (self.operator == "+"):
            self.result = int(self.firstValue) + int(self.secondValue)
        if (self.operator == "-"):
            self.result = int(self.firstValue) - int(self.secondValue)
        if (self.operator == "*"):
            self.result = int(self.firstValue) * int(self.secondValue)

    def printResult(self):
        print(self.result)

    def checkOperator(self):
        bGoodOperator = self.operator == "+" or self.operator == "-" or self.operator == "*"
        if (not bGoodOperator):
            print('Error: Operator must be ‘+’ or ‘-‘')
            exit()

    def prepareForPrint(self):
        #вначале все числа преобразуем в строки, так проще будет узнать их длину
        firstValueStr = str(self.firstValue)
        secondValueStr = str(self.secondValue)
        resultStr = str(self.result)
        #ищем элемент с максимальной длинной
        whiteSpaceTrimForSecondString = 2
        lenghtCol = max(len(firstValueStr), len(secondValueStr) + len(self.operator) + whiteSpaceTrimForSecondString)
        lenghtCol = max(lenghtCol, len(resultStr))
        #lenghtCol += 5 #зазор между колонками сделаем побольше

        #подготовим строки, которые сразу можно выводить на печать
        self.firstStringStr = createString(lenghtCol, firstValueStr)
        self.secondStringStr = self.operator + " " * (lenghtCol - len(self.operator) - len(secondValueStr)) + secondValueStr
        self.resultStr = createString(lenghtCol, resultStr)
        self.minusStr = "-" * (lenghtCol - 0)

def arithmetic_arranger(problems, condition=False):
    calc_array = []
    for problem in problems:
        calc = calcClass()
        calc.parseString(problem)
        calc_array.append(calc)

    for calc_elem in calc_array:
        calc_elem.checkOperator()
        

    for calc_elem in calc_array:
        calc_elem.calc()
        calc_elem.prepareForPrint()

    list_firstString = ""
    list_secondString = ""
    list_minus = ""
    list_result = ""
    for calc_elem in calc_array:
        list_firstString += calc_elem.firstStringStr + " "
        list_secondString += calc_elem.secondStringStr + " "
        list_minus += calc_elem.minusStr + " "
        list_result += calc_elem.resultStr + " "

    print(list_firstString)
    print(list_secondString)
    print(list_minus)
    print(list_result)


    
arithmetic_arranger(['3801 - 2 + 7', '123 + 49 ', '1234543535 + 123 + 9'], True)