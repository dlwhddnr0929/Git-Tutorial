def exchange(amount):
    coin_500 = amount // 500
    amount %= 500

    coin_100 = amount // 100
    amount %= 100

    coin_50 = amount // 50
    amount %= 50

    coin_10 = amount // 10

    print("500원 동전의 개수:", coin_500)
    print("100원 동전의 개수:", coin_100)
    print("50원 동전의 개수:", coin_50)
    print("10원 동전의 개수:", coin_10)

amount = int(input("동전으로 교환할 금액을 입력하세요: "))
exchange(amount)
