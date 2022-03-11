class calcClass(object):
    originalProblem = ""
    firstValue = ""
    secondValue = ""
    operator = ""
    result = 0

    firstValueStr = ""
    secondValueStr = ""
    operatorStr = ""
    resultStr = ""

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

    def printResult(self):
        print(self.result)

    def checkOperator(self):
        bGoodOperator = self.operator == "+" or self.operator == "-"
        if (not bGoodOperator):
            print('Error: Operator must be ‘+’ or ‘-‘')
            exit()

    def prepareForPrint(self):
        firstValueStr = str(self.firstValue)
        secondValueStr = str(self.secondValue)
        resultStr = str(self.result)
        lenghtCol = max(len(firstValueStr), len(secondValueStr))
        lenghtCol = max(lenghtCol, len(self.operator))
        lenghtCol = max(lenghtCol, len(resultStr))
        lenghtCol += 5 #зазор между колонками сделаем побольше

        self.firstValueStr = " " * (lenghtCol - len(firstValueStr)) + firstValueStr
        self.secondValueStr = " " * (lenghtCol - len(secondValueStr)) + secondValueStr
        self.operatorStr = " " * (lenghtCol - len(self.operator)) + self.operator
        self.resultStr = " " * (lenghtCol - len(resultStr)) + resultStr

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

    list_value1 = ""
    list_value2 = ""
    list_operator = ""
    list_result = ""
    for calc_elem in calc_array:
        list_value1 += calc_elem.firstValueStr
        list_value2 += calc_elem.secondValueStr
        list_operator += calc_elem.operatorStr
        list_result += calc_elem.resultStr

    print(list_value1)
    print(list_operator)
    print(list_value2)
    print(list_result)


    
arithmetic_arranger(['3801 - 2', '123 + 49', '1234543535 + 123'], True)