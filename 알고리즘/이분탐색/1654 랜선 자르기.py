
n,m = 4,11
board = [802,743,457,539]

# n, m = map(int, input().split())
# board = [int(input()) for i in range(n)]
board.sort()

start = 1 
end = max(board)   

result = 0

while start <= end:
    mid = (start + end) // 2
    now_m = 0
    for i in board:
        now_m += (i // mid)
    if now_m < m:
        end = mid -1
    else:
        start = mid+1
        result = mid
    print(f"mid = {mid} result = {result}")

print(result)