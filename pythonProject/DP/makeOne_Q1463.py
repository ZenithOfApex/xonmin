import sys

x = int(sys.stdin.readline())

ans = 0

dp = [0 for i in range(x + 1)]

for i in range(2, len(dp)):
    if i % 6 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i - 1] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    elif i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
    else:
        dp[i] = dp[i - 1] + 1
print(dp[x])
