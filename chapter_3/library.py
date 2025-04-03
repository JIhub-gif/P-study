datetime.date #연,월,일로 날짜를 표현할 때 사용하는 함수이다.

day.weekday()   #datetime.date 객체의 요일을 구할수있는 함수

day.isoweekday() #위 함수와 달리 0부터가 아닌 1부터 월요일을 나타내는 함수

time.time() #현재 시간을 실수 형태로 리턴하는 함수이다

time.localtime #time.time()이 리턴한 실수값을 사용해서 연,월,일,시,분,초...의 형태로 바꾸어 주는 함수

time.asctime() #time.localtime()이 리턴된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 리턴하는 함수

time.ctime() #위 함수를 간단하게 표시할수 있는 함수이다 asctime과 다른점은 항상 현재시간만을 리턴한다

tiem.strftime() #시간에 관련된 것을 세밀하게 표현한느 여러 가지 포멧코드를 제공한다

time.sleep() #일정한 시간 간격을 두고 루프를 실행시켜주는 함수

math.gcd() #최대공약수를 쉽게 구해주는 함수

math.icm() #최대공배수를 구해주는 함수 

random.random,randint() #난수를 발생시키는 모듈

random_pop() #리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그값을 리턴한다

ramdom.choice() #입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴한다

ramdom.sample() #리스트의 항목을 무작위로 섞고 싶을때 사용하는 함수이다

