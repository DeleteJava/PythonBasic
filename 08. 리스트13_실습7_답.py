# split은 따로 설정안하면 띄어쓰기 기준으로 잡는다.
# 설정하면, 해당문자를 기준으로 분리한다.
words=input("쉼표로 구분하여 단어들 입력 >> ")
words=words.split(",")
fword=input("찾아서 제거할 문자열 입력 >> ")
print("최초 리스트 :",words)
# 각 값에 대한 체크가 아니니 주의
if fword in words:
    index=words.index(fword)
    words.pop(index)
    print("제거된",end=" ")
    # words.remove(fword)
else:
    print("제거가 안된",end=" ")
print("리스트 :",words)