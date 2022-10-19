# 문자열 메서드 split() : 문자열을 쪼개서 리스트로 바꾼다.
# - 리스트가 나오기 때문에 리스트 운용방식을 적용한다.
values=input("값 여러개를 입력 >> ")
values=values.split()

# - 리스트는 수량이 존재하기 때문에, 수량이 모자르면 추가입력을 받는다.
if len(values)==1:
    print("값 2개 모자릅니다.")
    values.append(input("1번값 입력 >> "))
    values.append(input("2번값 입력 >> "))

values[0]=int(values[0])
values[1]=int(values[1])
values[2]=int(values[2])
values.sort()
print("최대값 :",values[-1])
print("최소값 :",values[0])