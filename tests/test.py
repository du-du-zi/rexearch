hangle_numbers = {'.':['.',0],'점':['.',0], '영':[0,0],'공':[0,0],'일':[1,0],'이':[2,0],'삼':[3,0],'사':[4,0],'오':[5,0],
'육':[6,0],'칠':[7,0],'팔':[8,0],'구':[9,0],
'0':[0,0],'1':[1,0],'2':[2,0],'3':[3,0],'4':[4,0],'5':[5,0],
'6':[6,0],'7':[7,0],'8':[8,0],'9':[9,0],
'십':[10,1],'백':[10**2,1],
'천':[10**3,1],'만':[10**4,1],'억':[10**8,1],'조':[10**12,1]}

def rep_num(price):
    #뒤에서부터 단위 수로 쪼개기
    number_table = [hangle_numbers[token] for token in price if token in hangle_numbers ]
    max_unit = 10
    
    idxs = list()
    
    for i,item in enumerate(number_table[::-1]):
        num = item[0]
        unit = item[1]
        if unit and num > max_unit:
            max_unit = num
            idxs.append(i)
    prev = 0
    res = 0
    length = len(number_table)
    for idx in idxs[::-1]:
        next = length-idx
        if number_table[prev:next] : res += find_FE(number_table[prev:next])
        prev = next
    if number_table[prev:] : res += find_FE(number_table[prev:])
    
    return res

# custom function
def find_FE(number_table):
    
    #단위 앞에 수가 생략된 경우 처리
    if number_table[0][1]:
        number_table.insert(0,[1,0])

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
    return eval(result) 
sl = ['4만5000','4.5만','4만5천','45000','사만오천원','천삼백억','8억7000만원','8억7000원','팔백오십만원','구천팔백사십칠만육천삼백이십오','이천 이백만원']    
# sl = ['4.5만']    
for s in sl:
    print(s,':', format(rep_num(s),','))

# print(find_FE('8십억 육천만'))
# print(find_FE('십억 6000만'))
# print(find_FE('10억 육천만'))
# print(find_FE('234억 육천만'))
# print(find_FE('천억 50만'))
# print(find_FE('십8만'))
# print(find_FE('십팔만'))
# print(find_FE('5억천3백'))
# print(find_FE('5억일천3백만'))
# print(find_FE('팔천오백만'))
# print(find_FE('일공공공칠일'))
# print(find_FE('백오'))
# print(find_FE('구'))
# print(find_FE('삼공공만'))
# print(find_FE('구천팔백사십칠만육천삼백이십오'))
# print(find_FE('5백1만'))
# print(find_FE('1.2억원'))
# print(find_FE('십이.공공구달러'))
# print(find_FE('13점영3엔'))
# print(find_FE('십3점7억'))
# print(find_FE('천200'))
# print(find_FE('천이백만원'))
# print(find_FE('일천 이백만'))