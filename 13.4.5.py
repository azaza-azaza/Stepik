def quick_merge(n):
    answer = list()
    for _ in range(n):
        answer += [int(c) for c in input().split()]
    answer.sort()
    # answer = ' '.join(answer)
    print(*answer)

n = int(input())
quick_merge(n)

