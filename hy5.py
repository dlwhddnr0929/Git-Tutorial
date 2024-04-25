def read_single_digit(digit):
    digits_kor = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    return digits_kor[digit]

def read_number(number):
    hundreds = number // 100
    tens = (number % 100) // 10
    ones = number % 10

    result = ""

    if hundreds != 0:
        result += read_single_digit(hundreds) + "백"

    if tens != 0:
        result += read_single_digit(tens) + "십"

    if ones != 0 or (hundreds == 0 and tens == 0):
        result += read_single_digit(ones)

    return result

def main():
    number = int(input("세 자리수 이하의 10진 정수를 입력하세요: "))
    if number > 999 or number < 0:
        print("잘못된 입력입니다.")
    else:
        print(read_number(number))

main()
