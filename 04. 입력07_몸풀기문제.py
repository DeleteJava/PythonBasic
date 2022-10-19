# 정수 3개를 입력을 받습니다.
# 1. 정수 3개의 합을 출력하세요.
# 2. 1. 에서 구한 합을 이용해 평균을 출력하세요
# 3. 2. 에서 구한 평균을 이용해 정수부와
#    실수부를 분리하여 출력하세요.
value1= int(input("첫번째 정수를 입력하세요 >> "))
value2= int(input("두번째 정수를 입력하세요 >> "))
value3= int(input("세번째 정수를 입력하세요 >> "))

# result1=int(value1+value2+value3)
# 우선순위 연산이 섞여 있기 때문에 괄호안부터 연산한다.
# 그 후 연산결과물에 대한 형변환을 처리해준다.
result1=value1+value2+value3
result2=result1/3


print("합 :",result1)
print("평균 :",result2)
print("정수부 :", int(result2))
print("실수부 :", result2% 1)


