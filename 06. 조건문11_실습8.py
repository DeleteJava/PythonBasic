# 문자열에 대해 값의 종류 판별은 상당히 어렵습니다.
# 여기서는 숫자문자와 . 문자의 조합에 대해서만
# 생각해주세요.

# in 연산자로 판별되는 것
# 123 vs 5.5.5, 3.14

# in 연산자로 판별안되는 것
# 5.5.5, 3.14

# count 메서드로 판별되는 것
# 123 vs 3.14 vs 5.5.5
value=input("값 입력 >> ")
count=value.count(".")
if count==0:
    value=int(value)
    print("정수 형변환 :",value)
    print(value,"+10 =",value+10)
elif count==1:
    value = float(value)
    print("실수 형변환 :",value)
    print(value,"+5 =",value+5)
else:
    print("정수/실수가 아닌 것 같습니다.")