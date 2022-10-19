# count(값) : 값의 수량을 정수로 준비해준다.
# 문자열의 메서드와 차이 : 값의 종류를 가리지 않는다.
# 중복된 것이 들어있는 리스트가 아니면 유용하지 않음
lst=[1,2,"A","ABC"]
print(lst.count(1))

# index(값) : 값의 위치를 찾아준다.
# count와 동일한 차이점이 존재한다.
# in을 이용해 체크해야 한다.
if 3 in lst:
    print(lst.index(3),"번째 인덱스!")
else:
    print("찾는 값이 없습니다.")

# sort() : 정렬시켜준다.
# 주의점 : 내부에 같은 종류의 값만 있어야 한다.
lst=[1,5,3,2]
lst.sort()
print(lst)
print("최소값 :",lst[0])    # 최대/최소값이 보장된다.
print("최대값 :",lst[-1])   # 순서가 중요하지 않을 때 유효하다.

# reverse() : 앞뒤 순서를 바꿔준다. 정렬안함
lst.reverse()
print(lst)