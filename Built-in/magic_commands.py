# %로 시작하는 command를 magic_command라고 부름

%time #한 번 쿼리가 돌아가는데 시간

%timeit # 여러 번 쿼리를 반복 시키고 평균 시간 알려줌

%prun #프로그램의 구조마다 시간이 얼마나 걸리는 지

%lprun #라인마다 얼마나 시간이 걸리는 지

!pip3 install line_profiler
%load_ext line_profiler #line 프로파일러 로드

%lprun -f function_name function_name() #함수 내 얼마나 시간 걸리는 지 결과 반환

!pip3 install memory_profiler
%load_ext memory_profiler #memory 프로파일러 로드

%memeit function_name()

%mprun
%mprun -f function_name function_name() #함수 내 얼마나 메모리 잡는 지 결과 반환



