n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int , input().split())))
ans = [sum(col) for col in zip(*l)]
if any(ans):
    print("NO")
else:
    print("YES")
