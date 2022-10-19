result=0
num=1
while True:
    limit=int(input("구할 양의 정수 입력 >> "))
    if limit>0:
        break
while num<=limit:
    result += num
    num+=1
print("%d까지의 합 : %d"%(limit,result))

while True:
    count=int(input("구할 양의 정수 입력 >> "))
    if count>0:
        break
result=0
print("%d까지의 합 :"%(count),end=" ")
# 값을 감소시켜도 동일하게 합을 구할 수 있다.
# 경우에 따라 더 효율적인 코드가 된다.
while count>=1:
    result += count
    count-=1
print(result)