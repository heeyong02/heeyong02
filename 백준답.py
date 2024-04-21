#백준 별찍기 1_2438
star = int(input('만들고 싶은 별 줄의 개수를 입력하세요: '))
for i in range(1, (star+1)):
    print('*' * i)
#백준 별찍기 2_2439
star = int(input('만들고 싶은 별 줄 개수: '))
for i in range(1, (star+1)):
    print(' ' * (star - i) + '*'*i)
#백준 별찍기 3_2440
star = int(input('만들고 싶은 별 줄 개수: '))
for i in range((star) ,0 ,-1):
    print('*'*i)
#백준 별찍기 4_2441
star = int(input('별 줄 개수: '))
for i in range((star),0,-1):
    print(' ' * (star-i) + '*'*i)
#백준 두 수 비교하기_1330
A,B = map(int, input().split())
if A > B:
    print('>')
if A < B:
    print('<')
if A == B:
    print('==')
#백준 윤년_2753
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('1')
else:
    print('0')
#백준 시험성적_9498
def get_score(g):
    if g >= 90:
        print('A')
    elif g >= 80:
        print('B')
    elif g >= 70:
        print('C')
    elif g >= 60:
        print('D')
    else:
        print('F')
score = int(input())
s = get_score(score)
