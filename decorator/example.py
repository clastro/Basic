# decorator는 함수를 변형하여 사용하는 함수

def returns(return_type):
  # Complete the returns() decorator , 데코레이터를 먼저 리턴해 주는 함수를 생성한다
  def decorator(func):
    def wrapper(*args, **kwargs): # wrapper는 입력 함수에 코드를 추가하여 실행시켜 주는 함수
      result = func(*args,**kwargs)
      assert type(result) == return_type
      return result
    return wrapper
  return decorator
  
@returns(dict)
def foo(value):
  return value

try:
  print(foo([1,2,3]))
except AssertionError:
  print('foo() did not return a dict!')
