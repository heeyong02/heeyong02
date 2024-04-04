def get_fixed_price(discount, dis_rate):
    fixde_price = discount / (1 - dis_rate / 100)
    return fixde_price

dis_rate = int(input("할인율은? "))
A_discounted = int(input("A 상품의 할인된 가격은? "))
B_discounted = int(input("B 상품의 할인된 가격은? "))

A_fixed_price = get_fixed_price(A_discounted, dis_rate)
B_fixed_price = get_fixed_price(B_discounted, dis_rate)

print("할인율은? ",dis_rate)
print("A 상품의 할인율은? ",A_discounted)
print("A 상품의 할인율은? ",B_discounted)
print("A 상품의 정가는", int(A_fixed_price), "원")
print("B 상품의 정가는", int(B_fixed_price), "원")
