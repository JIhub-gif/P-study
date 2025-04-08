def get_total_page(m,n):
    return m//n+1

print (get_total_page(5,10))
print (get_total_page(15,10))
print (get_total_page(25,10))
print (get_total_page(30,10))

#게시판 프로그램을 짜면서 게시물의 개수와 한페이지에 보여줄 게시물의 수를 입력으로 주어졌을때 총 페이지수를 출력하는 코드이다
#히지만 여기서 총 게시물은 30이고 페이지당 10개의 게시물을 보여줄 수 있다고 했을때 7번째 줄에서 4가 출력이 되는 결과가 출력이 된다
#이는 한 페이지에 보여 줄 게시물 수를 나눈 나머지 값이 0이 되므로 발생한다는 것을 유출 할 수 있다

def get_total_page(m,n):
    if m%n ==0:
        return m//n
    else:
        return m//n+1
    
print (get_total_page(5,10))
print (get_total_page(15,10))
print (get_total_page(25,10))
print (get_total_page(30,10))

#위와 같은 경우를 해결하고자 조건문을 추가 할 수 있다 만일 두값을 나눈 나머지가 0이라면 몫만을 턴하고 이외에 경우에는 +1을 해주어 리턴하도록 하는 것이다

#게시판 프로그램을 만드는 과정은 보다 복잡하지만 일단은 가장 간단한 페이지를 수를 구하는 방법을 시작하여 보기로 하였다. 