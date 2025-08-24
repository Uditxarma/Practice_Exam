"""Array Rotation"""

#Naive Approach (Extra Space, O(n)), Naive Approach (Extra Space, O(n))
arr = [1,2,3,4,5,6,7,8]
def rotation(arr, k):
    length = len(arr)

    k = k % length

    return arr[-k:]+ arr[:-k]

print(rotation(arr,k=3))
print("***************************")


#(a)Use Reversal Algorithm
def reverse(arr, left, right):
    while left< right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

def rotation_right(arr, k):
    length = len(arr)
    k= k%length

    reverse(arr, 0, length-1)

    reverse(arr, 0, k-1)

    return reverse(arr, k, length-1)

print(rotation_right(arr, k=3))
print("--------------------------------")

#Time: O(n)
#Space: O(1)


def rotate_left(arr, k):
    length = len(arr)
    k = k%length

    reverse(arr,0,k-1)
    reverse(arr,k,length-1)
    return reverse(arr,0, length-1)

print(rotate_left(arr, k=3))
print("--------------------------------")
#Time: O(n)
#Space: O(1)

"""
Summary
Right rotation → reverse whole → reverse first k → reverse rest
Left rotation → reverse first k → reverse rest → reverse whole
"""

#Rotate array left by 1 step
def reverse_left_1(arr,k):
    length = len(arr)
    reverse(arr,0, k-1)
    reverse(arr,k,length-1)
    return reverse(arr,0,length-1)

print(reverse_left_1(arr,k=1))

def rotate_left_by_one(arr):
    n = len(arr)
    first = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = first
    return arr
print('-------------------------')


#Rotate array right by 2 steps
def reverse_right_2(arr,k):
    reverse(arr, 0,len(arr)-1)
    reverse(arr,0,k-1)
    return reverse(arr, k, len(arr)-1)

print(reverse_right_2(arr,2))
def rotate_right_two(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

#Rotate array left by k steps (k may be larger than array size)and find the element at index 0
def reverse_left_by_k(arr, k):
    length = len(arr)
    k = k%length

    reverse(arr, 0, k-1)
    reverse(arr, k, length-1)
    return reverse(arr,0,length-1), arr[0]

print(reverse_left_by_k(arr,k=4))
def element_after_rotation(arr, k):
    n = len(arr)
    k = k % n
    rotated = arr[-k:] + arr[:-k]
    return rotated[0]
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


#(Tricky) Rotate matrix by 90° clockwise
mat = [[1,2,3],[4,5,6],[7,8,9]]

def rotation_90(mat):
    n = len(mat)

    #Transpose matrix
    for i in range(n):
        for j in range(i,n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    #Reverse each row
    for i in range(n):
        mat[i].reverse()

    return mat

rotated_matrix = rotation_90(mat)

for row in rotated_matrix:
    print(row)

#Time Complexity: O(n²)
#Space: O(1) (in-place)

'''
Q1: Left rotation by 1 → Shift elements
Q2: Right rotation by k → Use slicing or reversal algo
Q3: Left rotation by k (handle k > n) → modulo trick
Q4: Find element after rotation → rotate then pick index
Q5: Rotate matrix 90° → transpose + reverse rows
'''

print("----------------------------Prefix Sum---------------------------------")

'''
Prefix Sum & Sliding Window.
These two are must-know because they reduce brute force O(n²) solutions into efficient O(n) ones.
Prefix sum is an array where each element at index i stores the sum of all elements from 0 to i in the original array.
'''

#Naive O(n)
#Find sum of elements from index l to r, query = (1, 3)
arr = [2, 4, 6, 8, 10]

def sum_of_index(arr, l, r):
    return sum(arr[l:r+1])

print(sum_of_index(arr, 1, 3))

print("************************************")

#Prefix Sum Approach O(1) per query
aaro = [1,2,4,6,7,9]
def prefix_sum(arr):
    prefix = [0]*len(arr)
    prefix[0]=arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

print(prefix_sum(aaro))


def range_sum(prefix, l, r):
    if l == 0:
        return prefix[r]
    return prefix[r] - prefix[l-1]

arro1 = [2,4,6,8,10]
prefix = prefix_sum(arr)

print(range_sum(prefix, 1, 3))  # Output: 18
print(range_sum(prefix, 0, 4))  # Output: 30

#Preprocessing: O(n)
#Query: O(1)

#Subarray Sum equals Target

'''
Lesson 5: Sliding Window
When do we use Sliding Window?
When problem asks about subarrays of fixed or variable length.
Instead of recomputing sum/product/count each time → reuse results.
'''