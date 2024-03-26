#개념 확인 과제(연습문제 4.7)
def exchange(pay):
    n500 = pay//500
    pay %= 500

    n100 = pay//100
    pay %=100

    n50 = pay//50
    pay %= 50

    n10 = pay//10

    print('500원 동전의 개수: ', n500)
    print('100원 동전의 개수: ', n100)
    print('50원 동전의 개수: ', n50)
    print('10원 동전의 개수: ', n10)

def get_integer(prompt):
    return int(input(prompt))

#주 프로그램부

result = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(result)
