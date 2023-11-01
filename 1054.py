# Problem link: https://www.beecrowd.com.br/judge/pt/problems/view/1054
# Author: Alex Sousa Cruz (@alequisk)

def run_test(testcase):
    N, D = map(int, input().split())
    a = [(0, 1)] + [(int(s[2:]), 1 if s[0] == 'B' else 0) for s in input().split()] + [(D, 1)]

    def f(jmp):
        used = [False] * (N + 2)
        pos = 0
        while pos <= N:
            p = pos
            while p + 1 < N + 2 and a[p + 1][0] <= a[pos][0] + jmp:
                p += 1
            while p > pos:
                if p != N + 2 and a[p][0] - a[pos][0] <= jmp and not used[p]:
                    break
                p -= 1
            if p == pos:
                return False
            pos = p
            if a[pos][1] == 0:
                used[pos] = True

        while pos > 0:
            p = pos
            while p - 1 >= 0 and a[p - 1][0] >= a[pos][0] - jmp:
                p -= 1
            while p < pos:
                if not used[p]:
                    break
                p += 1
            if p == pos:
                return False
            pos = p
        return True

    lo, hi = 0, D
    ans = hi
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if f(mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(f"Case {testcase}: {ans}")


for i in range(1, int(input()) + 1):
    run_test(i)
