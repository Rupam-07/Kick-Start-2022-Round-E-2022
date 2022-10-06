import sys


def solve():
    n = int(sys.stdin.readline())
    print((n + 4) // 5)


def main():
    for i in range(int(sys.stdin.readline())):
        print(end=f'Case #{i+1}: ')
        solve()


if __name__ == '__main__':
    main()

#hello 11