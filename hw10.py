#연습문제 12.2
import pickle
import os
filepath = 'score.bin'

def input_scores():
    scores = []
    i = 0
    while True:
        n = int(input(f'#{i+1}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores        
def get_average(scores):
    total = 0
    for i in scores:
        total += i
    avg = total / len(scores)
    return avg
def show_scores(scores):
    for n in scores:
        print(n, end=' ')
    print()

#save/load
def save_data(scores,avg):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(avg, file)
def load_data():
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
        avg = pickle.load(file)
    return scores, avg

if os.path.exists(filepath):
    print('[파일 읽기]\n')
    scores, avg = load_data()
    print('[점수 출력]')
    print('\n개인점수: ',end='')
    show_scores(scores)
    print(f'평균: {avg:.1f}')
else:
    print('[점수 입력]')
    S = input_scores()
    avg = get_average(S)
    print('\n[점수 출력]')
    print('\n개인점수: ',end='')
    show_scores(S)
    print(f'평균: {avg:.1f}')
    save_data(S,avg)
