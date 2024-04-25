def get_name():
    name = input("한국에 오신 것을 환영합니다! 이름을 입력하세요: ")
    return name

def print_welcome_message(name):
    msg1 = f"안녕하세요, {name}님! 한국에 오신 것을 환영합니다!"
    msg2 = "여행이 즐거우시길 바랍니다!"
    
    box_length = len(msg1) if len(msg1) > len(msg2) else len(msg2)
    print("-" * (box_length + 4))
    print("-" + " " * (box_length + 2) + "-")
    print("- " + msg1 + " -" if len(msg1) == box_length else "- " + msg1 + " " * (box_length - len(msg1)) + " -")
    print("- " + msg2 + " -" if len(msg2) == box_length else "- " + msg2 + " " * (box_length - len(msg2)) + " -")
    print("-" * (box_length + 4))

name = get_name()
print_welcome_message(name)
