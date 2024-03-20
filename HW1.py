def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(반지름):
    넓이 = 3.14 * 반지름 * 반지름
    return 넓이

반지름 = get_radius('넓이를 구하고자하는 원의 반지름은?')
넓이 = get_circle_area(반지름)
print('반지름이', 반지름, '인 원의 넓이 = 3.14 *', 반지름, '*', 반지름, '=', 넓이)
