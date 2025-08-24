#Array Rotation

#Naive Approach (Extra Space, O(n)), Naive Approach (Extra Space, O(n))
arr = [1,2,3,4,5,6,7,8]
def rotation(arr, k):
    length = len(arr)

    k = k % length

    return arr[-k:]+ arr[:-k]

print(rotation(arr,k=9))


