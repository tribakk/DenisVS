def arithmetic_arranger(problems, condition=False):
    list_of_number1 = [] #a list where we will put all first numbers as ints from input
    list_of_number1_str = [] #a list where we will put all first number as strings from input
    list_of_number2 = [] #a list where we will put all second numbers as ints from input
    list_of_number2_str = [] #a list where we will put all second numbers as strings from input
    list_of_operators = []
    list_of_results = []
    lines_count = 0
    lines = '-'
    space = ' '
    list_of_lines = []
    if len(problems) >= 5:
        print('Error: Too many problems')
        exit()
    if '*' in str(problems):
        print('Error: Operator must be ‘+’ or ‘-‘')
        exit()
    if '/' in str(problems):
        print('Error: Operator must be ‘+’ or ‘-‘')
        exit()
    for problem in problems:
        problem_as_list = problem.split()
        number1 = problem_as_list[0]
        number2 = problem_as_list[2]
        if len(number1) > 4 or len(number2) > 4:
            print('Error: Numbers cannot be more than four digits')
            exit()
        for symbol in problem:
            if (symbol.isdigit() or symbol == '+' or symbol == '-' or symbol == ' ') == False:
                print('Error: Numbers must only contain digits')
                exit()
    for problem in problems:
        problem_as_list = problem.split()
        operator = problem_as_list[1]
        number1 = int(problem_as_list[0])
        number2 = int(problem_as_list[2])
        if len(problem_as_list[0]) > len(problem_as_list[2]): #determin how many spaces to add to the shorter number
            number1_1space = ((len(problem_as_list[0]) + 2) - len(problem_as_list[0]))*space + problem_as_list[0]
            list_of_number1_str.append(number1_1space)
            len_space = len(problem_as_list[0]) - len(problem_as_list[2])
            number2_space = operator + space  + space * len_space + problem_as_list[2]
            list_of_number2_str.append(number2_space)
        if len(problem_as_list[0]) < len(problem_as_list[2]): #determin how many spaces to add to the shorter number
            number2_1space = operator + space + problem_as_list[2]
            list_of_number2_str.append(number2_1space)
            len_space = len(problem_as_list[2]) - len(problem_as_list[0])
            number1_space = (len(number2_1space) - len(problem_as_list[0]))*space + problem_as_list[0]
            list_of_number1_str.append(number1_space)
        if len(problem_as_list[0]) == len(problem_as_list[2]): #determin how many spaces to add to equal numbers
            number1_1space = ((len(problem_as_list[2]) + 2) - len(problem_as_list[2]))*space + problem_as_list[0]
            list_of_number1_str.append(number1_1space)
            number2_1space = operator + space + problem_as_list[2]
            list_of_number2_str.append(number2_1space)
        list_of_number1.append(number1)
        list_of_number2.append(number2)
        list_of_operators.append(operator)
        if len(problem_as_list[0]) > len(problem_as_list[2]):
            lines_count = len(problem_as_list[0]) + 2
        else:
            lines_count = len(problem_as_list[2]) + 2
        list_of_lines.append(lines * lines_count)
    print('    '.join(list_of_number1_str))
    print('    '.join(list_of_number2_str))
    for item in list_of_lines:
        print(item, end='    ')
    print()
    if condition == True:  # If we have True in input we have to calculate results
        for index in range(len(list_of_operators)): #Calculating results by taking number1 and number2 from list_of_number1 and list_of_number2
            operator = list_of_operators[index]
            if operator == '+':
                result = list_of_number1[index] + list_of_number2[index]
                if len(str(list_of_number1[index])) > len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number1[index])) + 2) - (len(str(result))))*space + str(result)
                    list_of_results.append(result_str)
                if len(str(list_of_number1[index])) < len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number2[index])) + 2) - (len(str(result))))*space + str(result)
                    list_of_results.append(result_str)
                if len(str(list_of_number1[index])) == len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number1[index])) + 2) - (len(str(result))))*space + str(result)
                    list_of_results.append(result_str)
            if operator == '-':
                result = list_of_number1[index] - list_of_number2[index]
                if len(str(list_of_number1[index])) > len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number1[index])) + 2) - (len(str(result))))*space + str(result)
                    list_of_results.append(result_str)
                if len(str(list_of_number1[index])) < len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number2[index])) + 2) - (len(str(result)))) * space + str(result)
                    list_of_results.append(result_str)
                if len(str(list_of_number1[index])) == len(str(list_of_number2[index])):
                    result_str = ((len(str(list_of_number1[index])) + 2) - (len(str(result))))*space + str(result)
                    list_of_results.append(result_str)
        print('    '.join(list_of_results))
arithmetic_arranger(['3801 - 2', '123 + 49'], True)