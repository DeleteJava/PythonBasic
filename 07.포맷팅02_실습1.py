# 서식의 식별
# -> 반복되는 "문자열형태" 가 무엇인가?
form = "%s을 여기에 입력해주세요\n>> "
name1=input(form%("이름1"))
age1=input(form%("나이1"))
hob1=input(form%("취미1"))
# 단축키 ctrl + d : 드래그한 대상과 같은 곳에 커서잡기
# esc키로 커서잡기 취소
name2=input(form%("이름2"))
age2=input(form%("나이2"))
hob2=input(form%("취미2"))
form1="%5s%5s%5s"
print(form1%("이름","나이","취미"))
print(form1%(name1,age1,hob1))
print(form1%(name2,age2,hob2))
