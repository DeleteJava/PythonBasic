# 리스트의 역할 : 값들을 관리한다.
# 값 하나의 관리 : 변수가 수행
# 값 여러개의 통합관리 : 리스트
data=[
    int(input("정수1 입력 >> ")),
    int(input("정수2 입력 >> ")),
    int(input("정수3 입력 >> "))
    ]
result=data[0]+data[1]+data[2]
print(data)
print("총합 :",result)
print("평균 : %.2f"%(result/3))
