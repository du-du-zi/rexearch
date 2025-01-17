import os
from re import I
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # This is just for test env
import rexearch  # noqa : E402

rx = rexearch.Rexearch()
rx.load_json_file("tests/jay.test.rules.json")
sample_input = open("tests/jay.test.input.txt", mode="rt").read()

hangle_numbers = {'영':[0,0],'공':[0,0],'일':[1,0],'이':[2,0],'삼':[3,0],'사':[4,0],'오':[5,0],
'육':[6,0],'칠':[7,0],'팔':[8,0],'구':[9,0],'0':[0,0],'1':[1,0],'2':[2,0],'3':[3,0],'4':[4,0],
'5':[5,0],'6':[6,0],'7':[7,0],'8':[8,0],'9':[9,0],'십':[10,1],'백':[10**2,1],'천':[10**3,1],
'만':[10**4,1],'억':[10**8,1],'조':[10**12,1]}

# custom function
def Find_FE(price):
    number_table = [hangle_numbers[token] for token in price if token.isalnum()]
    
    def is_unit(table_index):
        return number_table[table_index][1]
    
    result = str(number_table[0][0])

    max_unit = 10
    for i in range(1,len(number_table)):
        if not is_unit(i) and is_unit(i-1):
            result += "+"
        elif is_unit(i):
            if number_table[i][0] > max_unit:
                max_unit = number_table[i][0]
                result = "("+result+")"
            if number_table[i][0] > number_table[i-1][0]:
                result += "*"
            else:
                result += "+"
        result += str(number_table[i][0])     
    return format(eval(result),',') 

def Find_tag(currency):
    return currency

rx.custom_functions["Find_FE"] = Find_FE
rx.custom_functions["Find_tag"] = Find_tag
results = rx.search(sample_input)

for result in results:
    print(result)