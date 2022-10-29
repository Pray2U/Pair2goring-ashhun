
def factorial(num:int):
    # update your code
    pass

def permutation(n:int, r:int):
    # update your code
    pass

def combination(n:int, r:int):
    # update your code
    pass

def infix2postfix(exp:str):
    # Using List, update your code
    pass

if __name__=="__main__":
    print("Assignment Check")
    print("="*30)
    
    exp = input("infilx expression: ")
    print(infix2postfix(exp))

    T = int(input("write factorial number : "))
    print(factorial(T))

    n, r = map(int, input("write permutation and combination number : ").split())
    print(permutation(n, r))
    print(combination(n, r))