# while에 while을 쓴다. 각 while은 서로 별개의 동작이다.
# 조건식을 공유할 경우, continue를 이용하면 while을 덜 쓸 수 있다.
# 입력을 하나 받거나, 중간에 되돌려야 할 때 유용하다.
while True:
    num1=int(input("양의 정수1 입력 >> "))
    if num1<=0:
        continue # 중간에 반복을 재시작시킨다.
        # 밑으로 불필요한 코드가 많을 때 사용된다.
    num2=int(input("양의 정수2 입력 >> "))
    if num2<=0:
        continue # 재시작이기 때문에 num1부터 다시 받는다.
    result=num1+num2
    if result%5!=0:
        break # 해당 구역 내의 while에 대해서만 작동한다.
    print("출력하지 않는다.")

print("5의 배수가 아닌 합 :",result)