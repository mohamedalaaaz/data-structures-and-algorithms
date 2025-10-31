from typing import List


class soltion:

    def coinchange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1] * (amount +1)
        dp[0] =0

        for a in range(1 ,amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] =min(dp[a] ,1 +dp[a-c])

        return dp[amount] if dp[amount] != amount +1 else -1



coins=[1,2,5]
a=11
c=soltion()
cs=c.coinchange(coins,a)
print(cs)


