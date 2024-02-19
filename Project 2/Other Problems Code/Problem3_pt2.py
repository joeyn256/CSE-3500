def BSM(nums):
    n = len(nums)
    
    # base case: if the list has only one element, return it
    if n == 1:
        return nums[0]
    
    # split the list into two sublists
    mid = n // 2
    left_sublist = nums[:mid]
    right_sublist = nums[mid:]
    
    # recursive calls to BSM on the left and right sublists
    max_left = BSM(left_sublist)
    max_right = BSM(right_sublist)
    
    # find the maximum sum across the middle
    max_left_middle = max_left_right = 0
    current_sum = 0
    for i in range(mid - 1, -1, -1):
        current_sum += nums[i]
        max_left_middle = max(max_left_middle, current_sum) # compute from middle to start
    
    current_sum = 0
    for i in range(mid, n):
        current_sum += nums[i]
        max_left_right = max(max_left_right, current_sum) # computer from middle to end
    
    max_middle = max_left_middle + max_left_right # this will take the max of the lsit iterating from the left to the right through the middle of the list
    
    # the max of the three sums found recursively will be the largest sublist of the values
    return max(max_left, max_right, max_middle)

#test using example given
nums = [4, -8, -5, 8, -4, 3, 6, -3, 2, -11]
result = BSM(nums)
print("max value of the sublist:", result)