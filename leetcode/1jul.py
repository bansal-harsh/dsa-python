//You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

//The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

//Return the minimum unfairness of all distributions
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cur = [0] * k
        n = len(cookies)

        def dfs(i, zero_count):
            # If there are not enough cookies remaining, return `float('inf')` 
            # as it leads to an invalid distribution.
            if n - i < zero_count:
                return float('inf')
            
            # After distributing all cookies, return the unfairness of this
            # distribution.
            if i == n:
                return max(cur)
            
            # Try to distribute the i-th cookie to each child, and update answer
            # as the minimum unfairness in these distributions.
            answer = float('inf')
            for j in range(k):
                zero_count -= int(cur[j] == 0)
                cur[j] += cookies[i]
                
                # Recursively distribute the next cookie.
                answer = min(answer, dfs(i + 1, zero_count))
                
                cur[j] -= cookies[i]
                zero_count += int(cur[j] == 0)
            
            return answer
        
        return dfs(0, k)
