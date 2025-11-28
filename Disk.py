# Exercise 2 – Disk.py
# Data Structure: Stack

# Initial Thoughts:

# Approach:
# - Initially i thought a simple heap would do the trick we could use if statements and keep adding elements to the heap and due to its auto-sort abilities in python we can enjoy a lower time complexity but as the input is a tuple here suddenly the question becomes overly complex
# i figured that the question structure is to figure out all the possibilities again and again to maintain optimal size hmm
# lets try using max operator.

# Additional Considerations:
# - placeholder


def disk_optimize(disks):
    """Optimize Disk by comparing each disk with every other disk to find all possible stacks and to select the best one"""
    stack = []
    max_height = 0
    best_stacks = [] # As our problem requires us to constantly check all possibilities we need a variable to track best stacks
    
    for i in range(len(disks)): # Iterate through all disks
        stack = [disks[i]]
        height = disks[i][2]
        
        for j in range(i+1, len(disks)):
            top_of_stack = stack[-1]
            new_disk = disks[j] # Use this disk to compare each disk
            
            if (new_disk[0] > top_of_stack[0] and new_disk[1] > top_of_stack[1] and new_disk[2] > top_of_stack[2]): # Check if new disk fulfils conditions to be added to the stack simultanoeusly also add the height
                stack.append(new_disk)
                height += new_disk[2]
                
        # After all iterations are completed for inner loop check if the current stack is the best stack 
        if height > max_height: # Update best height like we do in 1-D arrays if new height is greater than max height, replace old stack with new valeus
            max_height = height
            best_stacks = stack[::-1] # Reverse stack to have the smallest disk at the bottom
        elif height == max_height: # If height is equal to max height, we have found another optimal stack, add it to best stacks
            best_stacks += stack[::-1] # Reverse and add entire stack to the best_stacks as its a valid stack with the max height, removed append as it was adding additional brackets, this was a very annoying bug
                
    return best_stacks


if __name__ == "__main__":
    
    Input = [
    [2, 2, 5],   # Disk A: height 5
    [3, 3, 4],   # Disk B: height 4
    [4, 4, 1],   # Disk C: height 1
    [3, 3, 5],   # Disk D: height 5 (same height as A)
]
    Sample_Output = [[4, 4, 5], [3, 2, 3], [2, 1, 2]]
    
    result = disk_optimize(Input)
    print(result)
