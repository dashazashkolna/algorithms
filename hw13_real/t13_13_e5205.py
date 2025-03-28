MOD = 301907

def solve():
    s = input().strip()
    n = len(s)
    dp = {}
    dp[0] = 1
    for char in s:
        new_dp = {}
        for balance in dp:
            count = dp[balance]
            if char == '(':
                new_balance = balance + 1
                new_dp[new_balance] = (new_dp.get(new_balance, 0) + count) % MOD
            elif char == ')':
                new_balance = balance - 1
                if new_balance >= 0:
                    new_dp[new_balance] = (new_dp.get(new_balance, 0) + count) % MOD
            else:  # '?'
                # Заміна на '('
                new_balance = balance + 1
                new_dp[new_balance] = (new_dp.get(new_balance, 0) + count) % MOD
                # Заміна на ')'
                new_balance = balance - 1
                if new_balance >= 0:
                    new_dp[new_balance] = (new_dp.get(new_balance, 0) + count) % MOD
        dp = new_dp

    print(dp.get(0, 0) % MOD)

solve()