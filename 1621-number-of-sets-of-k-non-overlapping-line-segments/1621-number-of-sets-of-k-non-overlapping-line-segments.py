MOD = 10**9 + 7
LIMIT = 1999

fact = [0] * LIMIT
fact[0] = 1

for i in range(1, LIMIT):
    fact[i] = fact[i - 1] * i % MOD

inv = [0] * LIMIT
inv[-1] = pow(fact[-1], -1, MOD)

for i in range(LIMIT - 1, 0, -1):
    inv[i - 1] = inv[i] * i % MOD

def comb(n: int, m: int) -> int:
    return fact[n] * inv[m] * inv[n - m] % MOD

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n + k - 1, k * 2)