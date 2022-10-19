value=int(input("정수 입력 >> "))
# 팁1 : 관계연산자는 2개 연속사용했을 때
#     그게 무슨 의미인지 알아야 잘 쓸 수 있습니다.
# 팁2 : elif사용시 가장 좁은 조건을 첫번째로 쓴다.
# ex) 0 <= x < 10 -> x >=0 and x < 10
#     부정하면 x < 0 or x >=10
# 풀이1 : 크기 비교
if value<0:
    value*=-1
if value <10:
    print("한자리 수입니다.")
else:
    if value < 100:
        print("두자리 수입니다.")
    else:
        print("세자리이상의 수입니다.")
# 풀이2 : 문자열
count=len(str(value))
if count==1:
    print("한자리 수입니다.")
elif count==2:
    print("두자리 수입니다.")
else:
    print("세자리 이상입니다.")