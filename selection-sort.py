def selection_sort(numbers):
    for i in range(len(numbers)):
        min = numbers[i]
        for j in range(i, len(numbers)):
            if (numbers[j] < min):
                min, numbers[j] = numbers[j], min
        
        min, numbers[i] = numbers[i], min

if __name__=='__main__':
    nums = [34, 89, 21, 13, 90, 71, 37, 67, 45, 17]
    print(nums)
    selection_sort(nums)
    print(nums)
