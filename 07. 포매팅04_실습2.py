value1="1/4분기"
value2=3000
value3="상"
# 포매팅의 주 목적
# 문자열은 연속으로 문자가 배치되어 의사를 전달하는 것
# - 하나로 합쳐서 쉽게 구별할 수 있도록 도와준다.
print("""%s의 매출 : %d만원
%s의 평가 : %s"""%(value1, value2, value1, value3))
