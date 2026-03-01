def twoSums(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                return [i, j]


n = int(input("No of elements: "))
nums = []
result = []
for i in range(n):
    nums.append(int(input()))

target = int(input("Enter the target: "))
result = twoSums(nums, target)
print(result)