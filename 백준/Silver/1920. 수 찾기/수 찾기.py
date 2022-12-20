N = int(input())
board = list(map(int, input().split()))
board.sort()

m = int(input())
targets = list(map(int, input().split()))

def binary(target):
    left, right = 0, N-1
    while left <= right:
        mid = (left + right)//2
        if target == board[mid]: return True

        if target < board[mid]:
            right = mid -1 
        elif target > board[mid]:
            left = mid +1

for i in range(m):
    if binary(targets[i]):
        print(1)
    else:
        print(0)
