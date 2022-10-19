# 배수 판단은 나머지 연산결과물을 이용한다.
num=int(input("정수 입력 >> "))
# 들여쓰기 위치에 따라서, 최종 결과는 달라진다.
if num%2==0:
    print("2의 배수입니다.")
if num%7==0:
    print("7의 배수입니다.")
if num<15:
    print("15 미만입니다.")
if num>15:
    print("15 초과입니다.")
print("입력된 값 :",num)