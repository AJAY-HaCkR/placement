def find_missing_xor(nums):
    n = len(nums) + 1
    xor_all = 0
    xor_list = 0

    for i in range(1, n + 1):
        xor_all ^= i
    for num in nums:
        xor_list ^= num

    return xor_all ^ xor_list

# Example usage
nums = [1, 2, 4, 5]
print("Missing number is:", find_missing_xor(nums))
