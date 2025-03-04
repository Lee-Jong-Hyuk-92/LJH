# 게시판 페이징하기
# 함수 이름은? get_total_page
# 입력받는 값은? 게시물의 총 개수(m)
# 한 페이지에 보여 줄 게시물 수(n)
# 출력하는 값은? 총 페이지 수

# 내답
def get_total_page(m):
    if m%10!=0:
        page=m//10+1
    else:
        page=m//10
    return page

print(get_total_page(int(input('게시물이 총 몇개입니까?'))))

# 샘답
def getTotalPage(m,n):
    if m%n==0:
        return m//n
    return m//n+1
