# 표준 몸무게 공식
# m단위일 경우
# 키 * 키 * 22(or21)

# cm 단위일 경우
# (키/100) * (키/100) * 22(or21)
# (키 * 0.01) * (키 * 0.01) * 22(or21)
# 키 * 키 * 22(or21) * 0.0001

height=float(input("키 입력(m단위) >>"))
value = height**2
print("남성 표준 :",value*22,"KG")
print("여성 표준 :",value*21,"KG")
