# while : 조건문의 if를 while로 바꾼 형태
# 차이점 : 한번실행(if) vs 반복실행(while)

# 무한반복 : 몇번 반복할지 모른다. 많이 하는게 아님.
# - 입력받는 것과 연동하여 사용된다.
# - if와 while 비슷하지만 서로 절대로 같지 않음

values=input("값 3개를 입력하세요 >> ")
values=values.split()
while len(values)<3:
    print("3개가 아니어서 작동하지 않습니다.")
    values=input("값 3개를 입력하세요 >> ")
    values=values.split()
result=values[0]+values[1]+values[2]
print("합친 결과 :",result)

# 잘못된 케이스1 : 조건문으로 사용하기
# - 한번만 실행되도 충분한 것을 while로 만들어 좋은 점은 없다.
# num=int(input("음수면 양수로 바꿔 출력하는 코드\n>> "))
# if num<0:
#     num=-num
# print(num)

# 잘못된 케이스2 : 무슨 의도로 작성한 것인지 고려하지 않음
# - 한번만 나오면 되는 내용에 대해 while을 절대 쓰지 않는다.
# num=int(input("정수 입력 >> "))
# print("입력된 정수 :",num)
# if num%2==0:
#     print("2의 배수입니다.")
