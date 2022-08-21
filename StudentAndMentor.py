import sys

def solve():
    inp = sys.stdin.readline
    N = int(inp())
    R = list(map(int, inp().split()))
    a = [None] * N
    for i in range(N):
        a[i] = (R[i], i)
    a.sort()
    ans = [None] * N
    j = 0
    for _, i in a:
        while j + 1 < N and a[j + 1][0] <= R[i] * 2:
            j += 1
        if a[j][1] != i:
            ans[i] = str(a[j][0])
        elif j > 0:
            ans[i] = str(a[j - 1][0])
        else:
            ans[i] = '-1'
    print(' '.join(ans))


def main():
    for i in range(int(sys.stdin.readline())):
        print(end=f'Case #{i+1}: ')
        solve()


if __name__ == '__main__':
    main()
