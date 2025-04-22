'''Bubble Sort'''

def bubble_sort(numbers):
	for i in range(len(nums)):
		for j in range(len(nums)-1-i):
			if nums[j] > nums[j+1]:
				tmp = nums[j]
				nums[j] = nums[j+1]
				nums[j+1] = tmp

if __name__=='__main__': 
	nums = [34, 89, 21, 13, 90, 71, 37, 67, 45, 17]
	print(nums)
	bubble_sort(nums)			
	print(nums)
