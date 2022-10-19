# 추가문제1
# 내가 입력한 값부터 1씩 감소하는 1이상의 정수를
# 출력하세요.
# 단, 0이하의 값이 들어오면 재입력을 받습니다.
while True:
    num=int(input("0보다 큰 정수 입력 >> "))
    if num<=0:
        print("0보다 큰 값을 입력하세요.")
    else:
        break
value=num # 입력한 값을 보존할려면, 다른 변수에 복사
while num>=1:
    print(num, end=" ")
    num-=1 # 1씩 감소
print()

# 추가문제2
# 1부터 100까지의 정수 범위에서
# 내가 입력한 정수만큼 증가한 정수를 출력하세요.
# 0보다 더 크거나, 더 작아야 하며
# 0이 들어오면 재입력을 받습니다.
while True: 
    num=int(input("증가시킬 값 입력 >> "))
    if num!=0:
        break
    print("0이외의 값을 넣어주세요.")
result=1
while result <101 and result >= 1:
    print(result, end="")
    result=result+num
print()