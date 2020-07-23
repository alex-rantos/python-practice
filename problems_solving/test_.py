import random

def dfs(N, diff, path,memo):

    if diff%2==0:
        return False

    path.append(diff)
    if N == 0:
        return True
    if N in memo:
        path.extend(memo[N])
        return True
    for i in range(N, -1, -1):
        if dfs(N-i, i, path,memo):
            memo[N] = path
            return True
    return False
    
def solution(N):
    # write your code in Python 3.6
    if N == 1:
        return chr(ord('a') + random.randint(0,26))
    
    if (N-1)%2 == 1:
        return 'a'*(N-1) + 'b'
    
    for i in range(N-1, -1, -1):
        path = []
        if dfs(N-i, i, path,{}):
            print(path)
            if len(path)<= 26:
                ans = ''
                for i,num in enumerate(path):
                    ans += chr(ord('a') + i)*num
                return ans
    return ''

if __name__ == "__main__":
    print(solution(5))
    print("END")