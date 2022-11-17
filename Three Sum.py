# 給定一個由小至大且長度大於三的串列 lst，若其中三個數字的總和為 0 ，按照 index 大小由小到大將其輸出。

num = [int(i) for i in input().split()] # 給定一行輸入，內容為三個以上的整數由小至大排列，整數間以空格分開，請轉換為串列 lst

for i in range(0, len(num)):
    for j in range(1, len(num)):
        for k in range(2, len(num)):
            if num[i] + num[j] + num[k] == 0 and i < j < k:
                print(num[i], num[j], num[k]) # 輸出為數行，各包含三個整數，以空格分隔
