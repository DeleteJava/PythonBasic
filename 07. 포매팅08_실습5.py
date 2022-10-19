shape=input("모양 입력 >> ")
size=int(input("크기 입력 >> "))

print( ("ㅁ"*size+"\n")*size )
# 힌트 : 중복처리
# 일반포매팅은 어디에 적용해야 작동할까?
# - 연산처리한 결과물 출력
print( "%s" % ((shape * size + "\n") * size) )
# - 먼저 적용후 연산진행
print( (("%s" % (shape) * size + "\n") * size) )

# 고급포매팅은 일반포매팅처럼도 되지만, 어디에 넣어도 될까?
# - 연산처리한 결과물 출력
print( "{}".format((shape * size + "\n") * size))
# - 먼저 적용후 연산진행
print(("{}".format(shape) * size + "\n") * size)
# - 먼저 서식을 만들고 나중에 적용
print((("{0}" * size).format(shape) + "\n") * size)
print((("{0}" * size + "\n") * size).format(shape))