# 조건문 : 선택
# if : 추가실행
# if else : 무조건선택
# if elif else : 선택지 늘리기
# 실 사용법은 else가 있는가? 없는가?
# 있다 -> 선택지중 하나가 무조건 선택된다!
# 없다 -> 선택지들이 선택될 수 있지만, 안되고 문제없다.
sc1=float(input("국어 점수 입력 >> "))
sc2=float(input("영어 점수 입력 >> "))
sc3=float(input("수학 점수 입력 >> "))
avg=(sc1+sc2+sc3)/3
avg=int(avg*100)
if avg%10 >=5:
    avg+=(10-avg%10)
else:
    avg-=avg%10
avg/=100
if avg>=90:
    rank='A'
elif avg>=80:
    rank='B'
elif avg>=70:
    rank='C'
elif avg>=60:
    rank='D'
else:
    rank='F'
print("등급 :",rank+"등급")
print("평균 :", str(avg)+"점")