# format 메서드는 문자열의 기능이기 때문에 그냥 써도 되지만
# 가장 좋은 환경은 중복처리가 가능할 때이다!
value1=input("상품 입력 >> ")
value2=input("가격 입력 >> ")
value3=input("평가 입력 >> ")
# 포매팅 적용
print("""상품명\t: {0}
가격\t: {1}
평가\t: {2}
{0}의 가격은 {1}원이며
현재 {2}을 받고 있습니다.""".format(value1,value2,value3))
# 포매팅 미적용
print("상품명\t:",value1)
print("가격\t:",value2)
print("평가\t:",value3)
print(value1+"의 가격은",value2+"원이며")
print("현재",value3+"을 받고 있습니다.")
