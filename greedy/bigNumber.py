# 풀이 시간: 약 20 분 소요
# 알고리즘 설계 시간 보다는 파이썬 문법에 익숙하지 않아서 오래 걸렸다. 파이썬 사용에 익숙해져야겠다.

n, m, k = map(int, input().split(" "))
num = list(map(int, input().split(" ")))
max_num = max(num)  # O(N)
num.remove(max_num)  # O(N)
sec_max_num = max(num)  # O(N)


# 전체 복잡도: O(N + i)
def big_num(m, k):

    i = 0
    sum_num = 0
    while True:  # O(i)
        j = 0
        while j != k and i != m:
            sum_num += max_num
            j += 1
            i += 1
        if i == m:
            break
        sum_num += sec_max_num
        i += 1

    print(sum_num)


# 개선된 코드
# 복잡도 O(N)
def improved_big_num(m, k):
    sum_num = int(m/(k+1) * (max_num*k + sec_max_num) + max_num*(m % (k+1)))
    print(sum_num)
    # 8번 더하기 중복 3번
    # m/(k+1) * (max*k + sec) + max*(m%(k+1))


big_num(m, k)
improved_big_num(m, k)
