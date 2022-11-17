# 階乘
# 輸入有一行，包含一個正整數 num
# 輸出 num ! = result ( 5! = 120 )

num = int(input())
result = 1

for i in range(1, num+1):
    if num == 0 or num == 1:
        result = 1
    else:
        result *= i
        
print(f'{num}! =', result)
