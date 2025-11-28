import heapq

def heap_solution(boxes):
    boxes = boxes.copy()  # Create a copy to avoid modifying original
    res = [boxes[0]]
    heapq.heapify(res)

    for width, height, length in boxes[1:]:
        if width > res[-1][0] and height > res[-1][1] and length > res[-1][2]: 
            heapq.heappush(res, [width, height, length])
            
    res.sort(reverse=True)
    return res

def greedy_solution(boxes):
    boxes = boxes.copy()  # Create a copy to avoid modifying original
    boxes.sort()
    
    best_sequence = []
    
    # Try starting from each box
    for start_idx in range(len(boxes)):
        current_sequence = [boxes[start_idx]]
        
        for i in range(start_idx + 1, len(boxes)):
            width, height, length = boxes[i]
            last_box = current_sequence[-1]
            
            if width > last_box[0] and height > last_box[1] and length > last_box[2]:
                current_sequence.append([width, height, length])
        
        # Keep the longest sequence found
        if len(current_sequence) > len(best_sequence):
            best_sequence = current_sequence
    
    return best_sequence[::-1]

if __name__ == "__main__":
    Input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    print(greedy_solution(Input))
    print(heap_solution(Input))

# Time complexity analysis