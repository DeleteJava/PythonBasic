#        0 1 2 34 5 67 8 9 10
address="부산시 수영구 민락동"
#      -11 10 987 6 54 3 2 1
address=input("주소 입력 >> ")
# 상수값으로 설정된 슬라이싱은 규격에 맞아야만 할 수 있다.
# 필요한 위치는, 입력된 값을 기반으로 찾아서 슬라이싱한다.
# -> 변수로 대체한다.

# 실습2
index1=0
print("시 :",address[index1:index1+3])
index2=4
print("구 :",address[index2:index2+3])
index3=8
print("동 :",address[index3:index3+3])

# 실습3
word="Pyon Simple"
print(word[:2]+"th"+word[2:5]+"is"+word[4:])