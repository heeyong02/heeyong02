def read_single_digit(digit):
    if digit == 0:
        return '영'
    elif digit == 1:
        return '일'
    elif digit == 2:
        return '이'
    elif digit == 3:
        return '삼'
    elif digit == 4:
        return '사'
    elif digit == 5:
        return '오'
    elif digit == 6:
        return '육'
    elif digit == 7:
        return '칠'
    elif digit == 8:
        return '팔'
    elif digit == 9:
        return '구'
    else:
        return '오류'
    
def read_number(n):
    n_100 = n // 100
    n_10 = (n % 100) // 10
    n_1 = (n % 10)
    return n_100, n_10, n_1
    #한글 문자열 반환


#주 프로그램부
num = int(input('세 자리 정수 입력? '))
n_100, n_10, n_1 = read_number(num)
print(f'{read_single_digit(n_100)} {read_single_digit(n_10)} {read_single_digit(n_1)}')
