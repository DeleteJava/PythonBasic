lst=[]
lst.append(int(input("정수1 입력 >> ")))
lst.append(int(input("정수2 입력 >> ")))
lst.append(int(input("정수3 입력 >> ")))
print("최초 :",lst)
if 5 in lst: # 수량이 필요하면, count메서드로 대체한다.
    print("5가 있다!")
else:
    print("5가 없다!")
if 7 in lst:
    index=lst.index(7)
    lst[index]=int(input("새로운 값 입력 >> "))
    print("값이 바뀐 리스트 :",lst)