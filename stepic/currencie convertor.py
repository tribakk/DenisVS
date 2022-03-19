import urllib.request, urllib.parse, urllib.error
import http.client
import ast

conn = http.client.HTTPSConnection("currency-converter5.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "currency-converter5.p.rapidapi.com",
    'x-rapidapi-key': "dda745785dmshb273771362b051dp1616edjsn1bb92b90cf9b"
    }

print("Available currencies:\n US dollar = USD\n Canadian dollar = CAD\n Euro = EUR\n Russian Ruble = RUB\n British pound = GBP")
print()

while True:
    request_currencie1 = input("Enter currency #1: ")
    request_currencie2 = input("Enter currency #2: ")
    amount = input("Enter amount you want to convert: ")
    final_request = "/currency/convert?format=json&from=" + request_currencie1+"&to=" + request_currencie2 + "&amount=" + amount
    conn.request("GET",final_request , headers=headers)
    res = conn.getresponse()
    data = res.read()
    result = data.decode("utf-8")

    # Convert result string to dictionary
    result_as_dict = ast.literal_eval (result)

    result_inside = result_as_dict["rates"]
    currencie_key2 = 'rate'
    currencie_key3 = 'rate_for_amount'
    print()
    print('Current rate is',result_inside[request_currencie2][currencie_key2], request_currencie1, 'to', request_currencie2)
    print(amount,request_currencie1, 'is', result_inside[request_currencie2][currencie_key3], request_currencie2)
    print()
    request_to_try_again = input('Do you want to convert different pair?\nEnter Y to start over or S to stop ')
    if request_to_try_again == "Y" or request_to_try_again == "y":
        print()
        continue
    else:
        print()
        print('See you!')
        break

