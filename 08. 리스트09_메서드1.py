lst=[]
# 값을 추가하는 메서드
# 1. append(값) : 값을 후미에 추가해준다.
# result = lst.append(12) # 복사본 안나옴
# print(result)
lst.append(13) # 원본 갱신구조
lst.append(input("추가할 값 >> "))
# lst+=[input("추가할 값 >> ")]
print(lst)

# 2. insert(인덱스, 넣을 값) : 값을 인덱스에 밀어넣어준다.
lst.insert(1, 15) # lst[1:1]=[15]
print(lst)

# 3. extend(리스트와 호환되는 것) : 리스트랑 호환되는 것을 리스트에 합쳐준다.
# 호환되는 것 : 문자열, 튜플, 딕셔너리, 집합
lst.extend([21,22,23]) # 기존 리스트에 추가해준다.
# lst += list([21,22,23])
print(lst)

# 값을 제거하는 메서드
# 1. pop(인덱스) : 인덱스에 있는 값을 제거
lst.pop() # 안채우면 마지막을 제거한다
# lst[-1:] = []
print(lst)
lst.pop(2) # 특정 인덱스를 제거 
# lst[2:2+1] = []
print(lst)

# 2. remove(값) : 일치하는 값을 찾아 제거
lst.append(21)
lst.remove(21) # 여러개 있어도 제일 첫번째 하나만 제거
print(lst)
if 25 in lst: # 있는지 없는지를 체크하고 사용한다.
    lst.remove(25)
else:
    print("삭제할 값이 없습니다.")
print(lst)

# 3. clear() : 리스트 내부의 모든 것을 제거
# -> 이미 만들어진 리스트를 그대로 활용한다.
lst.clear() # lst[:]=[]
print(lst)

# append, insert, pop, remove 잘 기억하자!