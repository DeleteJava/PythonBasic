# 변수는 필요하면 의도적으로 값을 바꿀 수 있다
# 이미존재하는변수명 = 새로운값
# 왜?
# 원본을 유지할 필요가 있는가? 없는가?
num=100
print("정수값 :", num)
# 원본을 냅둬야 된다 -> 새로운 이름으로 새로운 변수를 생성한다.
num1=200
num2=num # 다른 변수에 저장된 값을 불러와 복사받는다.
print(num,num1,num2)
# 원본 필요없다 -> 덮어쓰기 한다.
num=300
print(num, num1, num2) # num2는 값을 복사하여 받았다. 별 상관없음.
