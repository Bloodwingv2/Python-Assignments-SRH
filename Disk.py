# Exercise 2 – Disk.py
# Data Structure: Stack

# Initial Thoughts:
# Initially considerd using a heap to manage and auto sort the disks but in practice it made more sense 
# to use a stack to keep track of the best possible combinations, as we need to constantly check all possibilities to attain all combinations.

# Approach:
# -Initially i thought a simple heap would do the trick we could use if statements and keep adding elements to the heap and due to its auto-sort abilities in python we can enjoy a lower time complexity 
# but as the input is a tuple here, with complex parameters and constraints it made more sense to use a stack.
# Going with this intuition i realized i had to scan through all disks again and again using nested loops to get our desired output.
# similar to how we store a maximum in 1-d arrays we store the best stack in the stack itself, pretty neat right?


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
    
    Input = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
    result = disk_optimize(Input)
    print(result)

# ============ TIME COMPLEXITY ANALYSIS PER FUNCTION ============
# disk_optimize():
# - Outer loop iterates through all disks as starting points: O(n)
# - Inner loop iterates through remaining disks to build stack: O(n)
# - Inside inner loop:
#     * Comparison and append operations are O(1)
#     * Reversing the stack when updating best_stacks: O(n)
#     * Concatenating to best_stacks: O(n) in worst case

# Time Complexity:
# - Best Case: O(n^2)
#   * If disks cannot stack (few comparisons succeed), and no max ties occur
# - Worst Case: O(n^3)
#   * If most disks can stack, and multiple stacks tie for max height, then we will see lots of stack reversals and concatenations

# Space Complexity:
# - Best Case: O(n)
#   * Only one stack is stored at a time, few disks in stack
# - Worst Case: O(n^2)
#   * Many stacks tie for max height, each up to n disks

# Final thoughts:
# In problems where every single possibility needs to be checked, a nested loop approach is often necessary. although
# usage of other data structures like can also help with discovering every single possibility but in this case,
# i believe the code in this particular case is highly readdable which satisfies our use-case.