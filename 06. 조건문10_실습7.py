# 문자열 메서드 index
# - 없으면 에러가 뜬다.

# 1) 문자열 메서드 count
# - 수량은 0 또는 양의 정수가 나온다.
word="ABC"
print(word.count("D"))
# 결과가 0이면 없다 / 0 이외의 값이면 있다.
# print(word.index("D"))
# - 여러개 있으면 그 수량을 세기 때문에 오래걸릴 수 있다.

# 2) 멤버쉽 연산자 in
# - 있다/없다를 결과로 주는 연산자. 작동구조는 count기반.
print("D" in word)

# 무언가로부터 찾았을 때 결과 없음이 나오는 이유
word1=input("찾는 단어 >> ")
word2=input("찾아볼 대상 >> ")
# in의 사용 용도 : 있는가/없는가?
if word1 in word2:
    print(word1,"이 있습니다.")
    print(word1,"의 위치 : 앞에서 ",word2.index(word1)+1,"번째")
else:
    print(word1,"이 없습니다.")