running = True
nums = [1,2,6,9,15,23]
def get_num(number):
    for i in range(len(nums)):
        if number == nums[i]:
            print(nums[1])
            
get_num(6)



 
def binary_search(start, end, number):
    mid = (end-start)/2
    if nums[mid] == number:
        print(nums[len(nums)/2])