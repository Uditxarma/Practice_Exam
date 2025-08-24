'''Check Palindrome using two pointers'''

text = "madam"

def palindrome(text) -> bool:
    left, right = 0, len(text)-1

    while left< right:
        if text[left] != text[right]:
            return False
        
        left += 1
        right -= 1
    return True

print(palindrome(text))

#Time Complexity: O(n)
#Space Complexity: O(1)


'''Pair Sum in Sorted Array'''
arr = [1, 2, 3, 4, 6]
target = 15

def pair_sum(arr, target)-> tuple:
    left, right = 0, len(arr)-1
    while left<right:
        sum = arr[left] + arr[right]
        if sum == target:
            return (arr[left],arr[right])
        elif(sum<target):
            left += 1
        else:
            right -= 1
    return None

print(pair_sum(arr,target))

#Time Complexity: O(n)
#Space Complexity: O(1)

'''Remove Duplicates from Sorted Array'''

arr1 = [1, 1, 2, 2, 3]
unique_list = []
def remove_duplicate(arr1)-> list:
    for i in len(arr1):
        unique_list.append(arr1[i])
        for j in len(arr1):
            if arr1[i] != arr1[j]:
                unique_list.append(arr1[j])
    

    return unique_list

print(remove_duplicate(arr1))