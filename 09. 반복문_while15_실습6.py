# 규칙성이 있다 - if else 없이 연산으로 처리된다.
# 규칙성이 없다 - 연산으로 불가능하니 if/else가 꼭 사용된다.

# while부터 만들면 잘 안보입니다. 그냥 해도 나오도록 만들어야 합니다.
num=1
result=0
value=int(input("약수를 구할 양의 정수 입력 >> "))
print("약수들의 목록")
while num<=value//2:
    if value%num==0:
        print(num, end=" ")
        result+=num
    num+=1
print(value)
result+=value
print("약수들의 합 :",result)