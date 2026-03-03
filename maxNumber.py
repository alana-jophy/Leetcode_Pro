def maxNumber(nums):

    if not nums:
        return None
    
    max = nums[0]

    max1 = float("-inf")
    max2 = float("-inf")

    # for i in range(len(nums)):      #for num in nums:
    #     if(max < nums[i]):              #if(max < num):
    #         maxSec = max
    #         max = nums[i]                   #max = num

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num

        elif num > max2 and num != max1:
            max2 = num
    return max1, max2

numbers = []

n = int(input("Enter the no. of elements: "))

print("Enter the numbers")
for i in range(n):
    numbers.append(int(input()))

maximum = maxNumber(numbers)

print(f"Maximum = {maximum}")