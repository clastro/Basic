#1. 처음 만들 때 모든 클래스에 값 전달
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    def get_count(self):
        return MyClass.count

#2. Magic Method or Special Method ( __로 시작해서 __로 끝나는 함수)

class Car:
    def __init__(self):
        print("자동차 제작 완료")

#2-1. __call__ 함수로 호출
class MyFunc:
    def __call__(self, *args, **kwargs):
        print("호출됨")
        

f = MyFunc()
f()
