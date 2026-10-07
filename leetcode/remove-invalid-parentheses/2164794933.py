class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            balance = 0

            for ch in s:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        q = deque([s])
        visited = {s}
        ans = []

        found = False

        while q:
            size = len(q)

            for _ in range(size):
                curr = q.popleft()

                if isValid(curr):
                    ans.append(curr)
                    found = True

                if found:
                    continue

                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue

                    next_s = curr[:i] + curr[i + 1:]

                    if next_s not in visited:
                        visited.add(next_s)
                        q.append(next_s)

            if found:
                break
        return ans