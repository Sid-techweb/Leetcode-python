class Solution:
    def canCompleteCircuit(self, gas, cost):
        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]

            if curr < 0:
                curr = 0
                start = i + 1

        if total >= 0:
            return start

        return -1