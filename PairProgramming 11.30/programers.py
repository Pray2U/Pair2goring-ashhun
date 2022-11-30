import itertools

def solution(babbling):
    answer = 0
    a = ["aya", "ye", "woo", "ma"]
    c = []
    bb = []
    
    for i in range(1, 5):
        bb = itertools.permutations(a, i)
        bb = list(map("".join, bb))
        c += bb
        
    for j in babbling:
        if j in c:
            answer += 1
    return answer