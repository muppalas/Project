"searching through an unorganized list"

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

# Input the array
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Input the target element
target = int(input("Enter the element to search for: "))

# Perform the search
result = linear_search(arr, target)

# Output the result
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
