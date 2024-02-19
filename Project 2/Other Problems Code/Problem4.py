def find_max_sublist(nums):# edge case
    if len(nums) < 2:
        return sum(nums), nums

    max_ending_at_next = max_list = nums[0] + nums[1] #base case
    start = end = 0

    for i in range(2, len(nums)):
        max_ending_at_next = max(nums[i], max_ending_at_next + nums[i]) #keep counter of ending at next as described in the algorithm

        max_list = max(max_list, max_ending_at_next) #keep running counter of the max list as described in the algorithm

        if max_list == max_ending_at_next: #update the new end of the running list by the update of max_list
            end = i

        if max_list == nums[i]: #update the new start of a list by the update of
            max_list
            start = i
            end = i

    return max_list, nums[start:end+1]
#test using example given
nums = [4, -8, -5, 8, -4, 3, 6, -3, 2, -11]
result = find_max_sublist(nums)
print("max value of the sublist:", result)