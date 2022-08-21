import sys


def solve():
    inp = sys.stdin.readline
    N = int(inp())
    P = inp()
    for i in range(N, 1, -1):
        if N % i == 0:
            L = N // i
            for j in range(L, N):
                if P[j] != P[j - L]:
                    break
            else:
                print(P[:L])
                return
    print(P[:N])


def main():
    for i in range(int(sys.stdin.readline())):
        print(end=f'Case #{i+1}: ')
        solve()


if __name__ == '__main__':
    main()
