# 입력에 무한반복이 적용되면 생기는 효과
# 1. 사용자에게 원하는 조건으로 입력되도록 <강요>한다.
# 2. 원하는 조건으로만 입력되기 때문에 뒤에 이어지는 코드의 조건문을
#    줄일 수 있다.

# while 종속문으로 if 가능하며, if 종속문으로 while 가능
# while 내부에 while 가능

print("0 이상의 양수만 출력하는 코드")
num=int(input("양수 입력 >> "))

# 입력받는 것에 대해 강력한 필터로써 작용한다.
# 원하는 것 외에는 무조건 거부한다.
while num<0:
    print("음수입니다.")
    num=int(input("다시 입력 >> "))

print("입력된 값 :",num)