cart = {}

def add_to_cart(item, quantity):
    cart[item] = quantity
    print(f"장바구니에 {item} {quantity}개가 담겼습니다.")

def view_cart():
    print("장바구니 보기:", cart)

def search_in_cart(item):
    if item in cart:
        print(f"{item}은(는) {cart[item]}개 담겨 있습니다.")
    else:
        print("해당 상품이 장바구니에 없습니다.")

while True:
    print("[구입]")
    item = input("상품명? ")
    if not item:
        break
    quantity = int(input("수량은? "))
    add_to_cart(item, quantity)

view_cart()

while True:
    print("[검색]")
    item = input("장바구니에서 확인하고자 하는 상품은? ")
    if not item:
        break
    search_in_cart(item)
