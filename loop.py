n = int(input("enter n: "))

print("\nNo Loop: ")
print("steps = 1 -> O(1)")
# 1. loop
print("\nOne Loop: ")

steps = 0
for i in range(n):
    steps += 1
print("steps = ", steps)
print("big-O: O(n)")
# 2. nested loops
print("\nTwo Loops: ")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print("steps = ", steps)
print("big-O: O(n^2)")

print("\nEasy rule:")
print(" 0 loops          -> O(1)")
print(" 1 loop           -> O(n)")
print(" 2 nested loops   -> O(n^2)")