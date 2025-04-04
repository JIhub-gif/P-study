def gugu(n):
    result=[]
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(gugu(2))


def gugu(n):
    result = []
    i=1
    while i<10:
        result.append(n*i)
        i=i+1
        return result


#프로그램을 코딩한다고 가정했을때 갈피를 잡지 못 할 수도 있다 그렇다면 가장먼저 생각해 볼 것은 "압력" 과 "출력" 을 어떻게 할지 고민해보는 것이 첫 단추일 것이다

#위 두개의 코드는 같은 결과값을 출력한다 gugu라는 함수를 선언하고 결과값을 리스트형태로 담고 append라는 함수를 사용하여 곱셈을 반복한다

#하지만 아래 코드에 비해 아래코드는 보다 간단하고 반복 함수의 개수를 줄일수 있다 처음부터 아래와 같은 코드를 작성 할 수 있다면 가장 좋겠지만

#복잡한 함수를 만들 때 원초적을로 접근한 뒤 단계적으로 접근하는 방식은 도움이 된다.
