def areDistinct(str,i,j):
    visited = [0]*(256)

    for k in range(i,j+1):
        if(visited[ord(str[k])]==True):
            return False

        visited[ord(str[k])] = True
    return True
def longest_substring(s: str) -> int:
    
    """"
    
    Implement the function longest_substring 
    using the provided longest_substring function to find 
    the length of the longest substring without repeating characters.

    """ 
    pass
    n = len(s)


    res = 0

    for i in range(n):
        for j in range(i, n):
            if (areDistinct(s, i, j)):
                res = max(res, j - i + 1)

    return res



