word="This is a apple!"
# replace(A , B) : A를 찾아서 B로 고친다.
print(word.replace("a","an")) # 일치하는 것을 전부 고친다
word="A    B C D E        F G"
print(word.replace(" ","")) # 모든 띄어쓰기를 제거함

# strip("ABCD") : 문자열 내의 일치하는 A,B,C,D가 있으면 양끝부터 제거해준다.
print(word.strip("AG "))
# ex)
address = "www.naver.com"
value=address.strip("wcom")
print(value)
value=value.strip(".")
print(value)

# split() : 문자열을 쪼개준다.
value=input("값 여러개 입력 >> ")
result=value.split()
print(result)