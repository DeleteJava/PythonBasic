# 숙제2.
# 내가 지정한 구간내에서 내가 지정한 만큼 증가하는 값을
# 출력하는 코드입니다.
start=int(input("시작값 입력 >> "))
end=int(input("끝값 입력 >> "))
step=int(input("증가값 입력 >> "))
# 아래의 while이 성립하는 값을 입력받도록 while무한반복을 구성하세요.
# 버려지는 경우의 수가 생기지 않도록 주의합니다.
# 힌트) 당장 아래의 코드에서 step이 음수이면 반복이 끝나지 않습니다.


# 이 유한반복 while은 절대 건드리지 않습니다.
while start<=end:
    print(start, end=" ")
    start+=step
