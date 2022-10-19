# 같은거 빼야 합니다.
num1=int(input("첫번째 정수 입력 >> "))
num2=int(input("두번째 정수 입력 >> "))
if num1 > num2: # 크기 비교시, >, <, >=, <= 이용합니다.
    # 변수 만들어 쓸 수 있음
    target="첫"
    head="2를"
    result = num1*2
else:
    # 단, 안만들어지는 경우가 생기면 에러가 생기니 주의
    target="두"
    head="3을"
    result = num2*3
print(target + "번째가 더 큽니다.")
print(head + " 곱한 결과 :",result)