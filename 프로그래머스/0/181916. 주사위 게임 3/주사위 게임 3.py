def solution(a, b, c, d):
    nums = [a, b, c, d]
    nums.sort()

    if nums[0] == nums[3]:
        return 1111 * nums[0]
    
    if nums[0] == nums[2] and nums[2] != nums[3]:
        return (10 * nums[0] + nums[3]) ** 2
    if nums[1] == nums[3] and nums[0] != nums[1]:
        return (10 * nums[3] + nums[0]) ** 2

    if nums[0] == nums[1] and nums[2] == nums[3] and nums[1] != nums[2]:
        return (nums[0] + nums[2]) * abs(nums[0] - nums[2])

    if nums[0] == nums[1] and nums[1] != nums[2] and nums[2] != nums[3]:
        return nums[2] * nums[3]
    if nums[1] == nums[2] and nums[0] != nums[1] and nums[0] != nums[3]:
        return nums[0] * nums[3]
    if nums[2] == nums[3] and nums[0] != nums[1] and nums[1] != nums[2]:
        return nums[0] * nums[1]

    return nums[0]
