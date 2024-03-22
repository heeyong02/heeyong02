
#사용자 정의 함수부_조건1
def get_radius(prompt):
    r = int(input(prompt))
    return r

#사용자 정의 함수부_조건2
def get_circle_area(r):
    return 3.14 * r * r

#주 프로그램부
r = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
area = get_circle_area(r)
print(f'반지름 {r}인 원의 넓이 = 3.14 X {r} X {r} = {area}')  #f-string 문자열 포맷팅방식
