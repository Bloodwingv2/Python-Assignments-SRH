# Sample code to test min heap addition for our usecase
import heapq

Input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
# Output = [[4, 4, 5], [3, 2, 3], [2, 1, 2]]

res = [Input[0]]
heapq.heapify(res)

for width, height, length in Input[1:]:
    if width > res[-1][0] and height > res[-1][1] and length > res[-1][2]:
        heapq.heappush(res, [width, height, length])
        
print(res)
    
