# 입력받는다 - 나중에 추가하면 된다.
# 1. 먼저 고정된 결과가 나오는 반복을 구성한다.
# 2. 무엇을 바꾸면 의도한 형태로 나오는지 확인하고
#    이를 입력받은 값으로 바꾼다.
# 주의 : 무조건 중복처리 아님.
# - 만들면 변수와 상수가 있을건데
#   상수는 중복처리 대상이 아님

# 프로그램 : 자료 -> 처리 -> 정보
# 코드/프로그램은 의도적으로 작성된 내용이다.
# 자료 : 정수
# 처리 : 반복
# 정보 : 배수의 목록
while True:
    value=int(input("정수 입력 >> "))
    if value>0:
        break
num=value
# 반복은 컴퓨터를 이용하기 위해 필수적인 제어문이다.
while num<=100:
    print(num, end=" ")
    num+=value
print()