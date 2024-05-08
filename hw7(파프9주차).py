shopping_bag = []
count_bag = []  #장바구니
total = {}
print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    else: 
        count = input('수량은? ')
        print(f'장바구니에 {item} {count}개가 담겼습니다.\n')
        shopping_bag.append(item)
        count_bag.append(count)
        total = dict(zip(shopping_bag, count_bag))
print(f'\n>>> 장바구니 보기:{total}\n')
print('[검색]')
re_item = input('장바구니에서 확인하고자 하는 상품은? ')
if re_item in total:
    print(f'{re_item}은(는) {total[re_item]}개 담겨 있습니다.')
