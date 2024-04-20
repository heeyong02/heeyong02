#사용자 정의 함수부
def multiplication_table1(n):
    for i in range(2, 6):
        print(f'{i}X{n} = {i* n:2d}', end ='\t')   
    print()
for n in range(1, 10):
    multiplication_table1(n)
print()  
def multiplication_table2(n):
    for i in range(6,10):
        print(f'{i}X{n} = {i* n:2d}', end ='\t')
    print()
for n in range(1, 10):
    multiplication_table2(n)
print()  
