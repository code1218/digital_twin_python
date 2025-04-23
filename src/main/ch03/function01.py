result = 10 + 20


def get10():
    return 5 + 3 + 2

result = get10() + 20

if get10() < 20:
    pass

def isEmpty(value):
    return str(value).strip() == ""


for text in ["", "a", "   ", "b"]:
    if isEmpty(text):
        print("비엇음")
        continue
    print(text)


def aaaa():
    pass

class Student:
    pass