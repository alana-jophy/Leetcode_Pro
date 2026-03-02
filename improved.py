def twoSums(nums, target):
	result = []
	
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if(nums[i] + nums[j] == target):
				result.append([nums[i], nums[j]])
	return result
				
        
    
	
nums = []

n = int(input("Enter the no. of elements: "))

for i in range(n):
	nums.append(int(input()))
	
target = int(input("Enter the target value: "))
result1 = []

result1 = twoSums(nums, target)
print(result1)