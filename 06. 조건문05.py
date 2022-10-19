# 경우의 수가 많을 경우, if 또는 else쪽에 조건문을 추가한다.
num1=int(input("첫번째 정수 입력 >> "))
num2=int(input("두번째 정수 입력 >> "))
if num1 > num2:
    print("첫번째가 더 큽니다.")
# else는 경우의 수의 쓰레기통과 동등하다.
# elif : else 내부의 조건문이 있을 때 들여쓰기를 줄이기 위한 제어문
# 1. 선택지 늘리기
# 2. 걸러내는 효과를 만들 수 있다.
elif num2 > num1:
    print("두번째가 더 큽니다.")
else:
    print("서로 같습니다.")
