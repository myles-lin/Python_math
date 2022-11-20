name_lst = input().split()
pay_dict = dict()
loan_dict = dict()

for name in name_lst:
    pay_dict[name] = 0

for name in name_lst:
    loan_dict[name] = {}
    for name_2 in name_lst:
        loan_dict[name][name_2] = 0
    
while True:
    try:
        spent = input().split()

        for i in range(0, len(spent)):
            try:
                spent[i] = int(spent[i]) # 如果 list 裡面的元素可以轉為 int，轉存為 int 
            except:
                if '%' in spent[i]:
                    spent[i] = int(spent[1] * int(spent[i][:-1]) / 100) # 把 百分比 都轉存為 int value
                pass
        
        if len(spent) == 2: # case 1: 所有人均分的狀況
            money = int(spent[1] / len(name_lst))
            for name in pay_dict:
                pay_dict[name] += money
                
            for name in loan_dict:
                if name != spent[0]: # 如果不是出錢的人 -> spent[0]，其他人都要計入欠款。
                    loan_dict[name][spent[0]] += money
        
        if len(spent) == 3 or (len(spent) > 3 and type(spent[3]) != int): # case 2: 特定人數均分的狀況
            money = int(spent[1] / (len(spent) - 1)) # spent[1] 不是人頭 所以要去除
            for name in spent:
                if type(name) == str:
                    pay_dict[name] += money
                    
            for name in spent:
                if name != spent[0] and type(name) == str: # 避開 spend[1] 不是人頭 (name)
                    loan_dict[name][spent[0]] += money
        
        if len(spent) >= 4 and type(spent[3]) == int: # case 3: 特定人數 依照特定比例分錢
            others_sum_money = 0 # 用來累計付款以外的人，需要付的總數
            for i in range(2, len(spent), 2):
                pay_dict[spent[i]] += spent[i+1] 
                others_sum_money += spent[i+1]
                loan_dict[spent[i]][spent[0]] += spent[i+1]  # loan_dict[ ][當下付錢的人]
                
            pay_dict[spent[0]] += (spent[1] - others_sum_money)
        
    except EOFError:
        break

def search_loan(x, y): # x 欠 y 多少錢
    return loan_dict[x][y]

ans_lst = []
i = 0
for people in loan_dict:
    tmp = 0
    ans_lst.append([])
    for creditor in loan_dict[people]:
        if people != creditor:
            money = search_loan(creditor, people) - search_loan(people, creditor)
            if money >= 0:
                tmp += money
            else:
                tmp += money
                ans_lst[i].append(creditor)
                ans_lst[i].append(str(-money))
    if tmp >= 0:
        tmp = '+' + str(tmp)
    ans_lst[i].append(str(tmp))
    i += 1

for i in pay_dict:
    print(i, pay_dict[i] , ' '.join(ans_lst[name_lst.index(i)]))
