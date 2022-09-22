#1. 숫자 계산

f"{2 * 37}" 

#2. 다른 포맷의 자료형을 한 문장 내에 출력

age = 74
name = '송'
f"The \"comedian\" is {name}, aged {age}."


#3. 변수 이름 안에 입력

peak = 'P'
peak_array = np.array(waves_cwt[f'ECG_{peak}'])

#4. 객체 치환

f"오늘은 {date.today()} 입니다."
f"오늘은 {date.today()!r} 입니다."
# __str__() 대신 __repr__() 호출
