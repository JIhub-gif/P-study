from operator import itemgetter

students = [
    {"name":"jane","age":22,"grade":"A"},
    {"name":"dave","age":32,"grade":"B"},
    {"name":"sally","age":17,"grede":"B"}

]

result = sorted(students,key=itemgetter("age"))
print(result)

#itemgetter('age')는 딕셔너리의 키인 age를 기즌으로 정렬하겠다는 의미이다

students=[
    ("jane",22,"A"),
    ("dave",32,"B"),
    ("sally",17,"B"),

]

result=sorted(students,key=itemgetter(1))
print(result)

#itemgetter(1)은 students의 아이템인 튜플의 두 번째 요소를 기준으로 정렬하겠다는 의미이다

from operator import attrgetter

class Sutdents:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

students = [
    students('jane',22,'A'),
    students('dave',32,'B'),
    students('sally',17,'B'),


]

result = sorted(students,key=attrgetter('age'))

#리스트의 요소가 튜플인 아닌 클래스의 객체라면 Students 객체의 age속으로 정렬하겠다는 의미이다
