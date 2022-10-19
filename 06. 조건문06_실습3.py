num1=int(input("제일 큰 정수 입력 >> "))
num2=int(input("제일 큰 정수보다 작은 정수1 입력 >> "))
num3=int(input("제일 큰 정수보다 작은 정수2 입력 >> "))
# 첫번째/두번째/세번째라는 표현은 쓰겠지만
# 절대로 변수명을 출력하지 않습니다.
# 그리고, 첫번째/두번째라는 표현도 잘 안씁니다.
if num1%num2==0:
    print(num2,"는 ",num1,"의 약수입니다.",sep="")
elif num1%num3==0:
    print(num3,"는 ",num1,"의 약수입니다.",sep="")
else:
    print(num1,"의 약수는 없습니다.",sep="")
# 재편성
if num1%num2!=0 and num1%num3!=0:
    print(num1,"의 약수는 없습니다.",sep="")
else:
    if num1%num2==0:
        result = num2
    else:
        result = num3
    print(result,"는 ",num1,"의 약수입니다.",sep="")
    