import sys

#yoo yoo python
def solve():
    inp = sys.stdin.readline
    N, P, M, Ar, Ac = map(int, inp().split())
    OP = [None] * 4
    K = [None] * 4
    OPf = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }
    for i in range(4):
        OP[i], K[i] = inp().split()
        K[i] = int(K[i])
        OP[i] = OPf[OP[i]]
    a = [[None] * N for i in range(N)]
    C = [None] * P
    for i in range(P):
        X, Y, C[i] = map(int, inp().split())
        a[X - 1][Y - 1] = i
    PP = 1<<P
    dp = [[None] * N for i in range(N)]
    dp[Ar - 1][Ac - 1] = [None] * PP
    dp[Ar - 1][Ac - 1][0] = 0
    for m in range(1, M + 1):
        nd = [[None] * N for i in range(N)]
        for x in range(N):
            for y in range(N):
                d = dp[x][y]
                if d is not None:
                    for p in range(PP):
                        dd = d[p]
                        if dd is None:
                            continue
                        if x > 0:
                            u = nd[x - 1][y]
                            v = OP[0](dd, K[0])
                            if u is None:
                                u = [None] * PP
                                nd[x - 1][y] = u
                                u[p] = v 
                            elif u[p] is None or u[p] < v:
                                u[p] = v
                            w = a[x - 1][y]
                            if w is not None and (p & (1 << w)) == 0:
                                v += C[w]
                                if (u[p | (1 << w)] is None
                                or u[p | (1 << w)] < v):
                                    u[p | (1 << w)] = v
                        if x + 1 < N:
                            u = nd[x + 1][y]
                            v = OP[3](dd, K[3])
                            if u is None:
                                u = [None] * PP
                                nd[x + 1][y] = u
                                u[p] = v 
                            elif u[p] is None or u[p] < v:
                                u[p] = v
                            w = a[x + 1][y]
                            if w is not None and (p & (1 << w)) == 0:
                                v += C[w]
                                if (u[p | (1 << w)] is None
                                or u[p | (1 << w)] < v):
                                    u[p | (1 << w)] = v
                        if y > 0:
                            u = nd[x][y - 1]
                            v = OP[2](dd, K[2])
                            if u is None:
                                u = [None] * PP
                                nd[x][y - 1] = u
                                u[p] = v 
                            elif u[p] is None or u[p] < v:
                                u[p] = v
                            w = a[x][y - 1]
                            if w is not None and (p & (1 << w)) == 0:
                                v += C[w]
                                if (u[p | (1 << w)] is None
                                or u[p | (1 << w)] < v):
                                    u[p | (1 << w)] = v
                        if y + 1 < N:
                            u = nd[x][y + 1]
                            v = OP[1](dd, K[1])
                            if u is None:
                                u = [None] * PP
                                nd[x][y + 1] = u
                                u[p] = v 
                            elif u[p] is None or u[p] < v:
                                u[p] = v
                            w = a[x][y + 1]
                            if w is not None and (p & (1 << w)) == 0:
                                v += C[w]
                                if (u[p | (1 << w)] is None
                                or u[p | (1 << w)] < v):
                                    u[p | (1 << w)] = v
                        u = nd[x][y]
                        if u is None:
                            u = [None] * PP
                            nd[x][y] = u
                            u[p] = dd
                        elif u[p] is None or u[p] < dd:
                            u[p] = dd
        dp = nd
    ans = None
    for x in range(N):
        for y in range(N):
            d = dp[x][y]
            if d is not None:
                d = d[PP - 1]
                if d is not None and (ans is None or ans < d):
                    ans = d
    if ans is None:
        print('IMPOSSIBLE')
    else:
        print(ans)


def main():
    for i in range(int(sys.stdin.readline())):
        print(end=f'Case #{i+1}: ')
        solve()


if __name__ == '__main__':
    main()
