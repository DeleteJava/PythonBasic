# 반복은 값의 목록이라는 것이 있으면...
# 이를 자동으로 처리할 수 있도록 해주는 기술이 된다.

# 1. 리스트에 적용한다 : 원하는 수량만큼 입력을 받고
# 이를 인덱싱하여 사용한다.
lst=[]
count=1
while count<=3:
    lst.append(int(input("정수%d 입력 >> "%(count))))
    count+=1
index=0
while index<=2:
    print(lst[index], end=' ')
    index+=1
print("\n")

# 2. 굳이 리스트에 저장하지 않고, 실시간으로 준비/입력한 값의 처리도 가능하다.
# 합을 구하는 논리 : 비어있는 곳/누적시킬 수 있는 곳에 누적시켜야 한다.
# 리스트 : []
# 숫자 : 0
result=0
num=1
while num<=5:
    result += int(input("%d번째 값 >>"%(num)))
    num+=1
print("최종결과 :", result, num)
# 파이썬 한정으로는 비슷한 논리로 누적시킬 수 있는 것은 누적된다.
# 문자 : ""
result=""
num=1
while num<=5:
    result += str(num) # input("%d번째 값 >>"%(num))
    num+=1
print("최종결과 :", result, num)
