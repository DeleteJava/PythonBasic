# 기본 포매팅은 단발성 + 중복이 없는 짧은 것에 유리하다.
# 고급 포매팅 : 기본 포매팅 + 중복처리
# - 문자열 메서드 format을 이용한다.

# 1) 기본적인 사용 : 오로지 배치만 시켜준다.
value1=123
value2=3.12999999999
value3="ABC"
print("정수 : {}\n실수 : {}\n문자열 : {}".format(value1,value2,value3))

# 2) 순서조작 및 중복처리
# (1) 번호부여 : 반드시 0번부터 부여한다.
# -> format에 배치되는 값의 순서가 고정되어 있을 때 유리하다.
print("{1} {0} {1}".format(value1, value2))

# (2) 이름부여 : 마음대로 부여한다.
# -> 배치되는 값의 순서가 지멋대로일 때 유용하다.
print("{값1} {값2} {값1}".format(값2=value2, 값1=value1))

# 3) 값의 모양을 바꾸기 위해 서식을 부여한다.
# -> 기본 포매팅과 문법이 상당히 많이 다르니 주의!
# {순서/이름:옵션서식문자}
print("{0:d} {0:d}".format(123))
# 좌중우 정렬가능
print("->{0:<5d}<-->{0:^5d}<-->{0:>5d}<-".format(123))
# {:.2f}를 추가하여 쓰면 유용하다
print("{:.2f}".format(value2))
