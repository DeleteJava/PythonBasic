lst=[3,5,7,9,1]
size=len(lst) # 리스트의 크기를 구한다.
print("저장된 값 :",end=" ")
index=-size
while index<=-1:
    print(lst[index], end=" ") # print(index, end=" ")
    index+=1
print()
result=0
index=-size
while index<=-1:
    result+=lst[index] # result += index
    index+=1
print("값들의 합 :",result)
print("값들의 평균 :",result/size)

print("저장된 값 :",end=" ")
index=0
while index < size:
    print(lst[index], end=" ") # print(index, end=" ")
    index+=1
print()
result=0
index=0
while index < size:
    result+=lst[index] # result += index
    index+=1
print("값들의 합 :",result)
print("값들의 평균 :",result/size)