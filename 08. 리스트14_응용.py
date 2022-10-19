# 리스트는 값을 바꿀 수 있다.
# -> 형변환이 된다면, 특정 부분만 바꾸는 것도 가능하다...
word="This is a apple"
converted=list(word)
print(converted)
index = converted.index('a')
converted[index]="an"
print(converted)
# 합연산을 처리할려니 너무 노가다이고 확정된 크기가 아니다...
result=converted[0]+converted[1]+converted[2]+converted[3]
print(result)
# 이를 자동으로 처리할 방법이 필요하다!
# -> 반복문을 이용해서 처리한다!

# 문자열로는 처리가 안된다.
# word=str(converted)
# word=word.strip("[]")
# word=word.replace("\'","")
# word=word.replace(",","")
# print(word)
# word=word.replace(" ","")
# print(word)