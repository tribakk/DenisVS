class calcClass(object):
    v1 = 0
    v2 = 0
    v3 = 0
    def calc(self):
        return self.v1 + self.v2 + self.v3
    
def calc2(v1, v2, v3):
    return v1 + v2 + v3
    

def arithmetic_arranger():
    c1 = calcClass()
    c2 = calcClass()

    c1.v1 = 10
    c1.v2 = 30
    c1.v3= 10000

    c2.v1 = 100
    c2.v2 = -10
    c2.v3 = -10000

    r1 = c1.calc()
    r2 = c2.calc()


    v1_array = []
    v2_array = []
    v3_array = []
    v1_array.append(10)
    v2_array.append(30)
    v3_arrya.append(10000)

    v1_array.apend(100)
    v2_array.apend(-10)
    v3_array.apend(-10000)

    r1_1 = calc2(v1_array[0], v2_array[0], v3_array[0])
    r1_2 = calc2(v1_array[1], v2_array[1], v3_array[1])
    
arithmetic_arranger()