"Arrat"

'''Traversing an Array'''
arr = [5, 1, 34, 10, 20, 30, 40, 50]

for i in range(len(arr)):
    print(arr[i], end=' ')
    
print("\n")

'''Insertion in Array'''
#Add element at the end (O(1) in Python list).
arr.append(60)
print(arr)

#Insert at specific position (O(n)).
arr.insert(2,15)
print(arr)

'''Deletion'''
arr.remove(30)      # removes first occurrence of 30
print(arr)

arr.pop()           # removes last element
print(arr)

'''Search in Array'''
#Linear Search(O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return {"At index:",i}
    return None

print(linear_search(arr, 40))


#Find the maximum element in an array.
#(a)
sorted_array = sorted(arr)
print("maximum is:", sorted_array[-1])

#(b)
def find_max(arr):
    max_val = arr[0]
    for i in arr:
        if i> max_val:
            max_val = i
    
    return max_val

print(find_max(arr))


#Write a function to find the minimum element in an array.
#(a)
sort = sorted(arr)
print("Minimum is:",sort[0])

#(b)
def find_min(arr):
    min_val = arr[0]
    for i in arr:
        if i<min_val:
            min_val = i
    return min_val

print(find_min(arr))

#Write a function to reverse an array.
#(a)with using [::-1]
print(arr[::-1])

#(b)Naive Approach (Using Extra Array), But this uses extra space.
def reverse(arr):
    reverse_array = []
    for num in range(len(arr)-1, -1, -1):
        reverse_array.append(arr[num])

    return reverse_array

print(reverse(arr))


#(c)Optimal Approach → Two Pointers
def optimal_approach(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr

print(optimal_approach(arr))
#Time: O(n)
#Space: O(1) (in-place)


#(d)Reverse only the first k elements
def reverse_k_element(arr, k=3):
    start = 0
    end = k-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr

print(reverse_k_element(arr,3))
print("______________________________")

#(e)Reverse the array in groups of size k                           ---> Noted count
def reverse_k_group(arr,k =3):
    l = len(arr)-1

    for i in range(0, l, k):
        left  = i
        right = min(i+k-1,l)
        while left< right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    return arr

print(reverse_k_group(arr, 3))
print("*******************************")

#(f)Reverse a subarray (from index l to r)
def reverse_subarray(arr,l,r):
    # left = l 
    # right = r
    while l< r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr

print(reverse_subarray(arr,l=2,r=5))


#(g)Check if an array becomes a palindrome after reversal
arr2 = [1, 2, 3, 2, 1]
arr1 = [1, 2, 3, 4, 5]

def reverse_palindrome(arr1)-> bool:
    left , right = 0, len(arr1)-1

    while left < right:
        if arr1[left] != arr1[right]:
            return False 
        left += 1
        right -= 1
        
    return True

print(f"{arr1}:",reverse_palindrome(arr1))

