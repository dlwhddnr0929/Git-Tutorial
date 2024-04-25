def get_fixed_price(discount_rate, discounted_price):
    fixed_price = discounted_price / (1 - discount_rate / 100)
    return fixed_price

discount_rate = float(input("할인율은? "))
discounted_price_A = int(input("A 상품의 할인된 가격은? "))
fixed_price_A = get_fixed_price(discount_rate, discounted_price_A)
discounted_price_B = int(input("B 상품의 할인된 가격은? "))
fixed_price_B = get_fixed_price(discount_rate, discounted_price_B)

print("A 상품의 정가는", round(fixed_price_A / (1 - discount_rate / 100)), "원")
print("B 상품의 정가는", round(fixed_price_B / (1 - discount_rate / 100)), "원")
