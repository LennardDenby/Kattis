def twoIntegerSum(A, x):
    low = 0
    high = len(A) - 1
    l = []
    
    while low < high:
        sum = A[low] + A[high]

        if sum == x:
            l.append((A[low], A[high]))
            high = high - 1
        elif sum > x:
            high = high - 1
        elif sum < x:
            low = low + 1
    
    print(l)
            

def main():
    A = [0,2,4,6,8,10]
    x = 10
    twoIntegerSum(A, x)

if __name__ == '__main__':
    main()