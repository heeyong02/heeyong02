import sys
N = int(input())
gain = list(map(int,sys.stdin.readline().strip().split()))
price = list(map(int,sys.stdin.readline().strip().split()))

sorted_gain = sorted(gain,reverse = True)
first_max = sorted_gain[0]
second_max = sorted_gain[1]
for i in range(N):
    if gain[i] == first_max:
        opp_cost = second_max-price[i]
    else:
        opp_cost = first_max - price[i]
    net_gain = gain[i] - (opp_cost+price[i]) 
    print(net_gain, end=' ')

'''세중이는 물건 사는 것을 좋아한다. 고양이를 키우고 싶어서 바나나 우유를 사거나 그림을 그리고 싶어서 삼다수 버즈 케이스를 사는 등 다양한 물건을 산다. 하지만 돌이켜보니 후회되는 구매도 많이 한 것 같아 경제적인 소비생활을 하려고 공부를 해왔다. 그래서 이제 순수익이 가장 크도록 물건을 구매하고 싶어 한다.

물건의 순수익을 구하기 위해선 먼저 물건의 기회비용을 구해야 한다. 어떤 물건의 기회비용은 자신을 제외한 나머지 물건의 이익 중 가장 큰 값에서 자신의 가격을 뺀 것이다. 순수익은 물건을 구매했을 때의 이익에서 그 물건의 기회비용과 가격을 뺀 것이다. 예를 들어 
3개의 물건이 있다고 하자. 각 물건을 구매했을 때의 이익이 각각280 270 240이고 가격이 각각 100 100 100이면 각 물건의 기회비용은 170 180 180이 된다. 순수익은 각각 10, -10, -40이다.
각 물건을 구매했을 때의 이익과 각 물건의 가격이 주어질 때, 각 물건의 순수익을 구해보자.
입력
첫 번째 줄에 물건의 개수 N이 주어진다.

두 번째 줄에 
N개의 물건을 각각 구매했을 때의 이익이 공백으로 구분되어 주어진다.

세 번째 줄에 
N개의 물건의 가격이 공백으로 구분되어 주어진다.

출력
첫 번째 줄에 각 물건의 순수익을 공백으로 구분하여 입력으로 주어진 순서대로 출력한다.

제한 
모든 이익과 가격은 
1 이상 10^6 이하의 정수이다.
예제 입력 1 
3
280 270 240
100 100 100
예제 출력 1 
10 -10 -40'''
