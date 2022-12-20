#1. 처음 만들 때 모든 클래스에 값 전달
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    def get_count(self):
        return MyClass.count
