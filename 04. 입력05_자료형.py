# 자료형 : 값의 종류
# 처음보는 것에 대해서 파악하는 법
# -> type() 함수를 이용한다.
num=123
fnum=3.14
word="Apple"
print(type(num)) # 처음보는 것은 이걸로 파악된다.
print(type(fnum)) # 형변환은 그 자료형을
print(type(word)) # 원하는 것으로 바꾸는 것


number = int(input("과일 갯수 >> "))

play = "나는 오늘 사과를 %d개 먹었습니다." % (number)

print(play , "하지만" , number , "개 더먹을 예정입니다")
