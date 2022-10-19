# 추가문제3
# 내가 지정한 구간 내에 있는 1씩 증가하는 정수를 출력하세요.
# 시작값과 끝값으로 따로 입력을 받습니다.
# 단, 시작이 끝보다 크면 <출력할 값이 없습니다.> 라고 출력합니다.
start=int(input("시작값 입력 >> "))
end=int(input("끝값 입력 >> "))
if start > end:
    print("출력할 값이 없습니다.")
else:
    while start<=end:
        print(start, end=" ")
        start+=1
    print()
# 추가문제4
# 1부터 15까지 범위의 정수만 출력합니다.
# 증감값을 입력받고
# 음수이면 15부터 감소하며
# 양수이면 1부터 증가합니다.
# 0이면 정수값을 재입력받도록 코드를 구성하세요.
while True:
    step=int(input("증감값 입력 >> "))
    if step!=0:
        break
    print("0은 안됩니다.")
if step<0:
    print("증감값이 음수일 때 반복문입니다.")
else:
    print("증감값이 양수일 때 반복문입니다.")