count=int(input("만두의 수량 >> "))
# 잘 안보일 때 일단 만들고 생각해본다.
# 1. 수량에 따라 나오는 값. 
# 2. 수량에 따라 달리 나오는 값.
# - 출력되는 종류 - 일부만 다르면 변수로, 아니면 그냥 방치
# - 연산에 사용되는 값 - 확실하게 변수로 빠진다.
if count<0:
    print("잘못되었다고 출력하던지, 재입력받던가 합니다.")
else:
    price=500*count
    print("할인전 가격\t: ",price,"원",sep="")
    if count>=100:
        per=20
        sale=0.8
    elif count>=50:
        per=10
        sale=0.9
    else:
        per=0
        sale=1
    print("할인률\t\t: ",per,"퍼센트",sep="")
    print("최종 가격\t: ", int(price*sale),"원",sep="")
