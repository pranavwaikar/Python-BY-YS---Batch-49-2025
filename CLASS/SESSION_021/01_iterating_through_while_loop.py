l1 = [10, 20, 30, 40, 50]

# Without while loop each element will need individual access
# This means that every element will need individual statement

n = l1[0]
print("Element at index 0: ", n)

n = l1[1]
print("Element at index 1: ", n)


n = l1[2]
print("Element at index 2: ", n)


n = l1[3]
print("Element at index 3: ", n)


n = l1[4]
print("Element at index 4: ", n)

# Doing the same using the loop
i = 0
while i < len(l1):
    print("Element at index", i, ":", l1[i])
    i+=1


# For loop practice before explanation
s = "Hello"
l = [10, 20, 30, 40, 50]      # List object can be modified - CRUD ops are allowed
t = (100, 200, 300, 400, 500) # Tuple can not be modified later - Its a READ ONLY - UNMODIFIED

# Using for loop to traverse string character by character
for c in s:
    print(c)

# Using for loop to traverse list element by element
for c in l:
    print(c)

# Using for loop to traverse tuple element by element
for c in t:
    print(c)

for l in l:
    print(l)

print("lsls",l)