# 산술연산자 : 수학적인 계산을 위한 연산자
# 주의사항 : 숫자끼리만 수학적인 계산이 가능하다

# 사용법
# 1) 한번 사용되면, 필요한 곳에 바로 작성하여 사용한다.
num=10
print("num + 3 =",num+3)
# 2) 여러번 사용되면, 변수에 저장하여 사용한다.
result1=num-3 # 연산식은 코드이다. 값이 아님.
num=14
print("결과1 :",result1) # 연산에 사용된 값이 바뀌어도, 영향이 없다.
print("비교1 :",num-3)

# 주의사항
# 1) 실수가 있으면 무조건 실수결과물이다.
print("어긋나는 경우1 :",2.5*10)
# 2) 나누면 무조건 실수이다.
print("어긋나는 경우2 :",num/2)
# 3) 몫/나머지는 정수끼리는 무조건 정수결과이다.
print("새로운 것1 :",num // 3)
print("새로운 것2 :",num % 3)
# 4) (공용규칙)연산자에는 우선순위가 있다
# 거듭제곱(제일 높다)
# (*, /) > (//, %)
# 덧셈/뺄셈
# -> 우선순위를 내 의도대로 동작시킬려고 한다면, 소괄호로 묶는다.
print("우선순위조작1 :",4*(3//2) )
print("우선순위조작2 :",(4*3)//2 )
# 5) (공용규칙)특별한 경우가 아닌 이상, 연산은 언제나 2개씩 처리되며
#             우선순위에서 밀리지 않거나, 동등할 경우
#             항상 왼쪽에서 오른쪽으로 진행한다
print("예시1 :",2+2+2) # 왼쪽부터
print("예시2 :",4+2) # 2개씩
print("에시3 :",6) # 처리가 된다












