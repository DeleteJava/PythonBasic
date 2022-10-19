# 메서드 : 특정 자료형에서만 쓸 수 있는 동작/기능(함수)
# 사용목적 : 사용하면 편하다!
# 사용방식 : 변수값.메서드명(필요한값)
word="AaAaBcCcDd"

# 1. count : 수량을 세어준다.
print(word.count("a")) # 대소문자 구별하니 주의

# 2. lower/upper : 대문자화/소문자화
upword=word.upper() # 원본을 이용해
loword=word.lower() # 복사본이 나온다.
print(upword, upword.count("A"))
print(loword, loword.count("a"))

# 3. index() : 정방향 인덱스번호를 찾아준다.
value1="3.142592"
value2="13.2543"
value3="132.22"
in1=value1.index(".")
in2=value2.index(".")
in3=value3.index(".")
print(value1, in1, value1[:in1+3]) # 잘 이용하면
print(value2, in2, value2[:in2+3]) # 매번 인덱스를 헤아릴 필요 없이
print(value3, in3, value3[:in3+3]) # 규칙성만 이용해서 처리할 수 있다
# 주의사항1 : 없는거 찾으면 터진다.
# -> 제어문을 이용해 있는지 없는지를 체크하고 진행한다.
print("." in word)
# -> 있으면 result=word.index(".") 이걸 실행한다.
# -> 없으면 실행하지 않는다...
# 주의사항2 : 중복이 있으면 첫번째만 찾는다.