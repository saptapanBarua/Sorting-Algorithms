'''Bubble Sort'''

def bubble_sort(numbers):
	for i in range(len(numbers)):
		for j in range(len(numbers)-1-i):
			if numbers[j] > numbers[j+1]:
				tmp = numbers[j]
				numbers[j] = numbers[j+1]
				numbers[j+1] = tmp

if __name__=='__main__': 
	nums = [34, 89, 21, 13, 90, 71, 37, 67, 45, 17]
	print(nums)
	bubble_sort(nums)			
	print(nums)
