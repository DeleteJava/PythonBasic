lst1=[1,2,3]
lst2=['A','B','C']
# 그냥 리스트를 만들어 쓴다 -> 변수가 늘어나면 메모리사용량이 증가한다.
# id() : 해당 변수의 고유번호를 값으로 준비해주는 함수
lst1[2:2]=lst2
print(lst1)
lst1[2:2+3]=[]
lst1[3:3]=lst2
print(lst1)
# <객체> 라고 취급되는 것들은 중복된다면서 빼버리면 대량 복사가 된다.
print(lst2)
lst2 += lst1[:3]
print(lst2)
lst2[3:]=[]
lst2[2:2]=lst1[:3]
print(lst2)