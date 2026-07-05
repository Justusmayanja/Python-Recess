import numpy as np

# Create numeric arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Array 1:", array1)
print("Array 2:\n", array2)

# Basic operations on array1
print("\nSum     :", np.sum(array1))
print("Average :", np.mean(array1))
print("Min     :", np.min(array1))
print("Max     :", np.max(array1))

# Add 5 to every element
array3 = array1 + 5
print("\nArray 1 + 5:", array3)

# Loop through array1
print("\nElements in Array 1:")
for num in array1:
    print(num, end=" ")
print()
