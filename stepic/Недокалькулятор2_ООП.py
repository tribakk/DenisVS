class calcClass(object):
    originalProblem = ""
    firstValue = ""
    secondValue = ""
    operator = ""
    result = 0
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
        calc_elem.printResult()
    
arithmetic_arranger(['3801 - 2', '123 + 49'], True)